from django.shortcuts import render
import pytesseract
from .forms import ImageUpload
import os
from PIL import Image

from django.conf import settings

def index(request):
    text = ""
    message = ""
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                image = request.FILES['image']
                image = image.name
                path = settings.MEDIA_ROOT
                pathz = path + "/images/" + image

                text = pytesseract.image_to_string(Image.open(pathz))
                text = text.encode("ascii", "ignore")
                text = text.decode()
                os.remove(pathz)
            except:
                message = "check your filename and ensure it doesn't have any space or check if it has any text"

    context = {
        'text': text,
        'message': message
    }
    return render(request, 'formpage.html', context)