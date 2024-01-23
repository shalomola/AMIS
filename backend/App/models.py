from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()
# Create your models here.



class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    username = models.CharField(max_length=30)
    staff_id = models.IntegerField(default=1)
    profileimg = models.ImageField(
        upload_to='profile_images', default='default-profile-pic.jpg')
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=60)
    dept = models.CharField(max_length=60)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    
class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Assets(models.Model):
    asset_name = models.CharField(max_length=100)
    asset_category = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=100)
    asset_manufacturer = models.CharField(max_length=100)
    date_purchased = models.DateTimeField()
    asset_issued = models.BooleanField(default=False)
    asset_image = models.ImageField(
        default="default.jpeg", upload_to='asset_images')

    def __str__(self):
        return self.asset_name

    def get_absolute_url(self):
        return reverse('assets-detail', kwargs={'pk': self.pk})


class AssetsIssuance(models.Model):
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(default=timezone.now)
    asset_assignee = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.asset)

    # def get_absolute_url(self):
    #     return reverse('assets-detail', kwargs={'pk': self.pk})
    

class Todo(models.Model):
    todo = models.CharField(max_length=300)

    def __str__(self):
        return self.todo