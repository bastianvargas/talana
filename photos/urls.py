from django.urls import path

#views
from .views import home, new_photo

urlpatterns = [
    path('', home, name="home"),
    path('new-photo', new_photo, name="new_photo")
]
