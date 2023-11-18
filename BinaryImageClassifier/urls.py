# Import necessary modules
from django.contrib import admin
from django.urls import path, include
from ClassifierModel import views
from django.conf import settings
from django.conf.urls.static import static

# Define URL patterns
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),
    # URL for uploading images, using the 'upload_image' view
    path('', views.upload_image, name='upload_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
