from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
import traceback2 as traceback
import random
import socket
from .models import *
import cv2
import os
from django.urls import resolve


# Create your views here.

# Create global variables
UPLOAD_URL = "./media/upload"

def index(request):

    context = {
        'pageName': 'index',
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def imageConvter(request):
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    # print(ip_address)

    # IpAddress.objects.create(ip_address = ip_address).save()
    current_url = resolve(request.path_info).url_name.split('-')[-1].upper()

    if request.method == 'POST':
        filename = request.FILES['image']
        Image.objects.create(image = filename).save()
        convertExtension(filename, current_url.lower())

    context = {
        'imageType': current_url,
        # 'imageDownload': convertImage,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def convertExtension(filename, current_url):
    url = f"./media/user_images/{filename}"
    name = os.path.basename(url).split('/')[-1]
    ext = os.path.splitext(name)
    image = cv2.imread(f"./media/user_images/{filename}")

    ext_name = ""
    match current_url:
        case 'png':
            ext_name = "png"
        case 'jpg':
            ext_name = "jpg"
        case 'jpeg':
            ext_name = "jpeg"
        case 'gif':
            ext_name = "gif"
        case 'webp':
            ext_name = "webp"

    cv2.imwrite(f"{UPLOAD_URL}/{ext[0]}.{ext_name}", image)

    return f"{ext[0]}.{ext_name}"

def pdfConvert(request):
    template = loader.get_template('pdf.html')
    return HttpResponse(template.render())