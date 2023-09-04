from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('image-to-png/', imageConvter, name='image-to-png'),
    path('image-to-jpg/', imageConvter, name='image-to-jpg'),
    path('image-to-jpeg/', imageConvter, name='image-to-jpeg'),
    path('image-to-gif/', imageConvter, name='image-to-gif'),
    path('image-to-webp/', imageConvter, name='image-to-webp'),
    path('image-to-pdf/', pdfConvert, name='image-to-pdf'),
]