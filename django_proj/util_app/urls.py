from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from . import views

app_name = "util_app"
urlpatterns = [
    path('upload/report/', views.upload_report, name='upload_report'),
    path('upload/device/', views.upload_device, name='upload_device'),
    path('upload/', views.upload_top, name='upload_top'),
]
