from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name="profile")
    bio = models.CharField(max_length=200)
    pic = ImageField(blank=True,manual_crop="")

    def __str__(self):
        return "Profile for {}".format(self.user.username)

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Job(models.Model):
    TIME_CHOICES = (
        ("part-time","part-time"),
        ("full-time","full-time"),
    )
    title = models.CharField(max_length = 40)
    company = models.CharField(max_length = 30,blank=True)
    company_pic = ImageField(blank=True, manual_crop="")
    category = models.ForeignKey(Category,on_delete = models.CASCADE,related_name="jobs")
    location = models.ForeignKey(Location,on_delete = models.CASCADE,related_name="jobs")
    time = models.CharField(max_length=20,choices=TIME_CHOICES,default="full-time")
    summary = models.TextField(blank=True)
    description = models.TextField()
    requirements = models.TextField()
    pub_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_job",args = [self.pk])

