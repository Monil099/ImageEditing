from django.db import models

# Create your models here.
class IpAddress(models.Model):
    ip_address = models.TextField(max_length=255)

class Image(models.Model):
    image = models.ImageField(upload_to='user_images')