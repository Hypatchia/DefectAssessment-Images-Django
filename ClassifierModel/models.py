from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    # Your existing fields
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Add this field for timestamp
    
    
    
    def __str__(self):
        return self.image.name  