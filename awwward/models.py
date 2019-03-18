from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to='images/', null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    objects = models.Manager()
        

    def __str__(self):
        return self.user.username

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Projects(models.Model):
    name = models.CharField(max_length =30,null=True)
    image = models.ImageField(upload_to = 'images/',null=True)
    description = models.TextField(null=True)
    link = models.URLField()
    poster = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    # design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    # usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    # content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    # vote_submissions = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    class Meta:
        ordering = ["-id"]
