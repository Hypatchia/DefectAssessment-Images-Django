# Create your views here.
from django.shortcuts import render
from django.http import  JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import io
import numpy as np
from PIL import Image
from .forms import UploadImageForm
from .models import UploadedImage 
from django.db.models import Max
import tensorflow as tf
import h5py
from azure.storage.blob import BlobServiceClient
from django.utils import timezone
import os
from django.conf import settings

AZURE_BLOB_STORAGE_CONNECTION_STRING = os.environ['AZURE_BLOB_STORAGE_CONNECTION_STRING']
AZURE_BLOB_CONTAINER_NAME_MEDIA =  os.environ['AZURE_BLOB_CONTAINER_NAME_MEDIA']
AZURE_BLOB_CONTAINER_NAME = os.environ['AZURE_BLOB_CONTAINER_NAME']

#AZURE_BLOB_STORAGE_CONNECTION_STRING = settings.AZURE_BLOB_STORAGE_CONNECTION_STRING
#AZURE_BLOB_CONTAINER_NAME_MEDIA =  settings.AZURE_BLOB_CONTAINER_NAME_MEDIA
#AZURE_BLOB_CONTAINER_NAME = settings.AZURE_BLOB_CONTAINER_NAME

# Define a function to load the model from Azure Blob Storage
def load_model_from_blob():
    """
    Loads a machine learning model from Azure Blob Storage.

    Outputs:
    - Loaded machine learning model (tf.keras.models.Model)
    """


    print('loading model from blob')
    connection_string = AZURE_BLOB_STORAGE_CONNECTION_STRING
    container_name = AZURE_BLOB_CONTAINER_NAME
    
    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Define the blob name for the model file
    blob_name = "BinaryClassifierModel.h5"

    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)

    # Get a reference to the blob
    blob_client = container_client.get_blob_client(blob_name) 

    # Download the H5 file to a bytes buffer
    blob_data = blob_client.download_blob()

    model_bytes = io.BytesIO()

    # Read the blob data into the bytes buffer
    blob_data.readinto(model_bytes)
    print('model downloaded')
    # Reset the buffer position to the beginning
    model_bytes.seek(0)

    # Load the model from the bytes buffer using h5py
    with h5py.File(model_bytes, 'r') as f:
        loaded_model = tf.keras.models.load_model(f)
    print('model loaded')
    return loaded_model

# Load the model
loaded_model = load_model_from_blob()

# Get the input shape of the model
input_shape = loaded_model.input_shape[1:3] 

# function to preprocess images for machine learning
def preprocess_image(image, target_size):
    """
    Preprocesses an image for machine learning.

    Inputs:
    - image: Input image (tf.Tensor)
    - target_size: Target size for the preprocessed image (tuple)

    Outputs:
    - Preprocessed image (tf.Tensor)
    """

    # Resize the image to the target size
    resized_image = tf.image.resize(image, target_size)

    # Convert the image to dtype tf.float32 
    preprocessed_image = tf.cast(resized_image, tf.float32) 
    return preprocessed_image

# function to convert rgb images to grayscale using tf
def convert_to_grayscale(image):

    """
    Converts a color image to grayscale.

    Inputs:
    - image: Input image (tf.Tensor)

    Outputs:
    - Grayscale image (tf.Tensor)
    """
    # Convert the image to grayscale using tf 
    grayscale_image = tf.image.rgb_to_grayscale(image)
    return grayscale_image


def upload_image_to_blob(file_content, blob_name):
    """
    Uploads an image to Azure Blob Storage.

    Inputs:
    - file_content: Image file content (bytes)
    - blob_name: Name of the blob in Azure Blob Storage (str)

    Outputs:
    - True if the upload is successful, False otherwise
    """
    connection_string = AZURE_BLOB_STORAGE_CONNECTION_STRING
    container_name_media = AZURE_BLOB_CONTAINER_NAME_MEDIA

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name_media)

    # Upload the image to the container
    try:
        container_client.upload_blob(name=blob_name, data=file_content,connection_timeout=14400,overwrite=True)
        return True  # Upload successful
    except Exception as e:
        print(f"Error uploading image to Azure Blob Storage: {str(e)}")
        return False  # Upload failed

    



def upload_image(request):
    """
    Handles image upload, processing, and classification.

    Inputs:
    - request (HttpRequest): The HTTP request object containing the uploaded image.

    Outputs:
    - JsonResponse: A JSON response containing prediction results or an error message.
    """

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
        
            image_instance = form.save(commit=False)

            image = Image.open(image_instance.image)
       
            # Convert the image to grayscale
            grayscale = convert_to_grayscale(image)

            # Preprocess the image for the model
            preprocessed_image = preprocess_image(grayscale, target_size=input_shape)

            # Expand dimensions to match model input
            preprocessed_image = np.expand_dims(preprocessed_image, axis=0)
            print('predicting...')
            
            # Perform the image classification and get a prediction
            prediction = loaded_model.predict(preprocessed_image)
            print('prediction done')
            # Determine the predicted label based on the prediction score
            if prediction >= 0.5:
                predicted_label = 'ok_front' 
            elif prediction < 0.3:
                predicted_label = 'defected_front'
            else:
                predicted_label = 'unknown, there must be an error'

            # Save the image instance to the database
            image_instance.save()

            # Convert the original image to bytes
            original_image_data = image.tobytes()
            # Create a unique blob name based on the prediction label
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")

            blob_name = f"{timestamp}_{predicted_label}"

            # Upload the image to Azure Blob Storage
            upload_result = upload_image_to_blob(original_image_data, blob_name)
            print('upload done')
            if upload_result:
                print('returning response')
                # Image was successfully uploaded to Azure Blob Storage
                # Save the image instance with the blob_name
                image_instance.blob_name = blob_name
                image_instance.save()
                response_data = {
                    'prediction': predicted_label,
                    'prediction_probabilityOK': prediction.tolist()[0][0],
                    'prediction_probabilityDefect': 1- prediction.tolist()[0][0],    
                }
                return JsonResponse(response_data)
            else:
                # Handle the case where the image upload to Blob Storage failed
                response_data = {
                    'error': 'Failed to upload image to Azure Blob Storage',
                }
                return JsonResponse(response_data, status=500)  # Return a 500 Internal Server Error status
   
    else:
        form = UploadImageForm()
    return render(request, 'ClassifierModel/upload_image.html', {'form': form})


