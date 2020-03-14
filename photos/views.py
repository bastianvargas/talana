from django.shortcuts import render
from django.shortcuts import redirect

#models
from .models import Photo

#forms
from .forms import PhotoForm

def home(request):
    photos = Photo.objects.all()
    data = {
        'photos':photos
    }
    return render(request, 'photos/home.html', data)

def new_photo(request):
    data={
        'form': PhotoForm()
    }

    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, files=request.FILES)
        if photo_form.is_valid():
            photo_form.save()
            data['message'] = 'Guardado Correctamente'
            return redirect('home')
    return render(request, 'photos/new_photo.html', data)
