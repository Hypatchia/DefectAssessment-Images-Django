## Project Overview

This project is aimed at providing a simple yet effective solution for assessing product defects using computer vision and deep learning techniques.

* The trial version of this application can be accessed at Pump Defect Assessment. 

* Product images can be uploaded by users, and whether the product is defective or defect-free will be predicted by the system.

* The source code and resources for the web application, including the deep learning model used for prediction, are contained in this repository.

## Built with:

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Latest-blue?style=flat&logo=tensorflow)](https://www.tensorflow.org/)
[![Azure](https://img.shields.io/badge/Azure-Latest-blue?style=flat&logo=microsoft-azure)](https://azure.microsoft.com/)
[![Django](https://img.shields.io/badge/Django-Latest-blue?style=flat&logo=django)](https://www.djangoproject.com/)


## Dataset

The deep learning model was trained on a dataset of product images. The dataset consists of labeled RGB images of Submersible Pump Impellers, with each image categorized as either "defected front" or "ok front."

* The structure of the dataset is as follows:
A link to the dataset:

## Image Processing:

To prepare the images for training and prediction, the following processing steps were performed:

* Images were loaded into their respective training and validation directories using TensorFlow data generator.
* Resizing: Images were resized to a consistent size to ensure uniform input for the neural network.
* Conversion to Grayscale: Images were converted to grayscale to reduce the complexity and size of the data while retaining essential features.

## Training a Convolutional Neural Network for Binary Image Classification

* A Convolutional Neural Network (CNN) was designed to perform binary image classification. The CNN is trained on the labeled dataset, learning to distinguish between defective and defect-free products.

* The CNN architecture is as follows:

## Model Evaluation:

* To evaluate the performance of the trained model and ensure its accuracy and reliability in predicting product defects, the metrics used were accuracy, precision, and recall.

Details of the results are shown in the figure:

The results of training curves are also available below:

## Web App

* A defect assessment web system was built using Django that allows the upload of an image of a product, processing, and then prediction of its status as 'defected or defect-free.'

* The process includes loading the pretrained deep learning model from Azure Blob storage, preprocessing the image, converting it to grayscale, and then making the final prediction of the product's status as "defected" or "defect-free."

* A screenshot of the app is available:

* The app can be accessed at:

## Deployment

* The final web application has been deployed on Azure App Services, ensuring scalability and reliability. 
* Azure Blob Containers are used for storing deep learning models and product images for seamless integration with the web application.

## Setup to run 

* Clone Repository
* Navigate to directory
* Run in terminal
* Create Virtual Environemeent & Activate it
* Install requirements
~~~
pip install requirements.txt
~~~
* Run App
~~~
python manage.py runserver
~~~
## Resources:

## Contact
