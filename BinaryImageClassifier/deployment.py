# Import necessary modules
import os
from .settings import *
from pathlib import Path
from azure.storage.blob import BlobServiceClient

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Configure Azure Blob Storage settings
AZURE_BLOB_STORAGE_CONNECTION_STRING = os.environ['AZURE_BLOB_STORAGE_CONNECTION_STRING']
AZURE_BLOB_CONTAINER_NAME_MEDIA =  os.environ['AZURE_BLOB_CONTAINER_NAME_MEDIA']
AZURE_BLOB_CONTAINER_NAME = os.environ['AZURE_BLOB_CONTAINER_NAME']

# Create an Azure Blob Service Client from the connection string
azure_blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_STORAGE_CONNECTION_STRING)

# Configure Django settings
SECRET_KEY = os.environ['SECRET']
# Define the allowed hosts and CSRF trusted origins
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

# Define the middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Define installed applications
INSTALLED_APPS = [
    'ClassifierModel.apps.ClassifiermodelConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



ROOT_URLCONF = 'BinaryImageClassifier.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BinaryImageClassifier.wsgi.application'

# Configure static files settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticroot'

# Parse Azure PostgreSQL connection string and configure the database settings
connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'],
        'HOST': parameters['host'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
    }
}



CRISPY_TEMPLATE_PACK ='bootstrap4'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
