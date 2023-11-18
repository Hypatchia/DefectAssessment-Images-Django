# Import necessary modules
import os
from pathlib import Path    
from azure.storage.blob import BlobServiceClient
from decouple import config
# Build the base directory path
BASE_DIR = Path(__file__).resolve().parent.parent
# Configure Azure Blob Storage settings

AZURE_BLOB_STORAGE_CONNECTION_STRING = config('AZURE_BLOB_STORAGE_CONNECTION_STRING')   
AZURE_BLOB_CONTAINER_NAME_MEDIA = config('AZURE_BLOB_CONTAINER_NAME_MEDIA')
AZURE_BLOB_CONTAINER_NAME = config('AZURE_BLOB_CONTAINER_NAME')
# Create an Azure Blob Service Client from the connection string
azure_blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_STORAGE_CONNECTION_STRING)
# Configure Django settings
SECRET_KEY = 'django-insecure-b^++$%3gi(l=och0t1x@&!kkh$3_y*)tm21@c57=-cjwzl8qu1'
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = []
# Define the installed applications
INSTALLED_APPS = [
    'ClassifierModel.apps.ClassifiermodelConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# Configure Cross-Origin Resource Sharing (CORS)
CORS_ORIGIN_ALLOW_ALL = True
# Define the middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Configure the root URLconf
ROOT_URLCONF = 'BinaryImageClassifier.urls'

# Configure templates
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

# Define the WSGI application
WSGI_APPLICATION = 'BinaryImageClassifier.wsgi.application'

# Configure the database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configure static files settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ClassifierModel', 'static'),
]
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticroot'
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Configure media files settings

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Configure Crispy Forms template pack
CRISPY_TEMPLATE_PACK = 'bootstrap4'