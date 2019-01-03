from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name="profile")
    bio = models.CharField(max_length=200)
    pic = ImageField(blank=True,manual_crop="")

    def __str__(self):
        return "Profile for {}".format(self.user.username)


