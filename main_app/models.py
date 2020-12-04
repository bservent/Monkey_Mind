from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Meditation(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=250, default= '')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class Profile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.DateField(auto_now_add=True)
    meditation = models.ForeignKey(Meditation, default = '', on_delete=models.CASCADE)
    imageURL = models.ImageField(upload_to = 'profile_image', blank=True, default = '', null = True)

    def __str__(self):
        return self.name
        
     

