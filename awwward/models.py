from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to='images/', null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
