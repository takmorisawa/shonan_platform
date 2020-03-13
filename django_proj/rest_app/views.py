from django.shortcuts import render

import django_filters
from rest_framework import viewsets,filters

from rest_app.models import Spot,Post
from rest_app.serializer import SpotSerializer,PostSerializer

class SpotViewSet(viewsets.ModelViewSet):
    queryset=Spot.objects.all()
    serializer_class=SpotSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
