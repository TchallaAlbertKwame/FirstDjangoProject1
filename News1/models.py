from django.db import models
from django.utils import timezone


# Create your models here.


class News(models.Model):
    Author = models.CharField(max_length=30)
    Title = models.CharField(max_length=25)
    Description = models.TextField()

    pub_date = models.DateField(default=timezone.now())  # adding date to the site
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.Author


class SportNews(models.Model):
    Author = models.CharField(max_length=30)
    Title = models.CharField(max_length=25)
    Description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    # date = models.DateField(auto_now_add= True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.Author


class RegistrationData(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Phone = models.CharField(max_length=150)

    def __str__(self):
        return self.username
