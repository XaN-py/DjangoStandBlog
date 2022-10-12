from django.db import models
from django.contrib.auth.models import User


class TypeWork(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_work = models.ManyToManyField(TypeWork)
    image = models.ImageField(upload_to="profile/image", blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=200,blank=True )

    def __str__(self):
        return self.user.username

