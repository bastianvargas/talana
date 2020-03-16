from django.db import models

class Photo(models.Model):

    nick_name = models.CharField(max_length=50)
    pet_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='pet_photo')
    likes = models.IntegerField(default=0)

    def __str__(self):
            return '{}'.format(self.nick_name)

    def save(self):
            self.nick_name = self.nick_name.upper()
            super(Photo, self).save()

    class Meta:
        verbose_name_plural = "Photos"
