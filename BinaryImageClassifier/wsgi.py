"""
WSGI config for BinaryImageClassifier project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
 
# Set default settings module based on whether it's running locally or in Azure
settings_module = "BinaryImageClassifier.deployment" if 'WEBSITE_HOSTNAME' in os.environ else 'BinaryImageClassifier.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
