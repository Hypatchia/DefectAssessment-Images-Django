from azure.storage.blob import BlobServiceClient
from django.conf import settings
import os
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Get the Azure Blob Storage connection string and container name from Django settings
connection_string = settings.AZURE_BLOB_STORAGE_CONNECTION_STRING
container_name = settings.AZURE_BLOB_CONTAINER_NAME

def upload_h5_to_azure(file_path, blob_name):
    """
    Uploads an H5 file to Azure Blob Storage.

    Inputs:
    - file_path (str): The local file path of the H5 file to be uploaded.
    - blob_name (str): The name of the blob in Azure Blob Storage.

    Returns:
    - bool: True if the upload is successful, False if the upload fails.
    """
    # Create a BlobServiceClient using the Azure Blob Storage connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)
    
    try:
        # Open the H5 file in binary mode and upload it to Azure Blob Storage
        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data)
        return True  # Upload successful
    except Exception as e:
        print(f"Error uploading H5 file to Azure Blob Storage: {str(e)}")
        return False  # Upload failed

# Main function
if __name__ == "__main__":
    # Define the local file path of the H5 model
    models_dir = os.path.join(BASE_DIR, 'ClassifierModel', 'static', 'ml_models')
    model_path = os.path.join(models_dir, 'ImageClassifier.h5')
    
    # Define the name for the blob in Azure Blob Storage
    blob_name = "BinaryClassifierModel.h5"
    
    # Upload the H5 file to Azure Blob Storage and print the result
    if upload_h5_to_azure(model_path, blob_name):
        print("H5 file uploaded successfully to Azure Blob Storage")
    else:
        print("H5 file upload to Azure Blob Storage failed")
