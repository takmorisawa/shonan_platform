from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from . import views

app_name = "util_app"
urlpatterns = [
    path('upload/', views.upload, name='upload'),
]
