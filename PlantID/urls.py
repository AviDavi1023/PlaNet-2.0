from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('howtouse', views.howtouse, name='howtouse'),
    path('upload', views.upload, name='upload')

]