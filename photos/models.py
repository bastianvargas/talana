from django.db import models

class Photo(models.Model):

    nick_name = models.CharField(max_length=50)
    pet_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='pet_photo')
    likes = models.IntegerField(default=0)
