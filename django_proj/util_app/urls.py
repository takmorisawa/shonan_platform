from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from util_app.views import DeviceUploadViewSet, ReportUploadViewSet, SupportUploadViewSet
from . import views

app_name = "util_app"
urlpatterns = [
    path('upload/device/process/', DeviceUploadViewSet.upload),
    url('upload/device/.*', DeviceUploadViewSet.validate),

    path('upload/report/process/', ReportUploadViewSet.upload),
    url('upload/report/.*', ReportUploadViewSet.validate),

    path('upload/support/process/', SupportUploadViewSet.upload),
    url('upload/support/.*', SupportUploadViewSet.validate),

    path('upload/', views.upload_top, name='upload_top'),
]
