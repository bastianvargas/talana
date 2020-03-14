from django.contrib import admin

# Register your models here.


from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    fields = ['nick_name', 'pet_name', 'photo', 'likes']

admin.site.register(Photo, PhotoAdmin)
