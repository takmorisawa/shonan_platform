from django.shortcuts import render

import django_filters
from rest_framework import viewsets,filters
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_app.models import Product,Series,Device,Report
from rest_app.serializer import ProductSerializer,SeriesSerializer,DeviceSerializer,ReportSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    queryset=Series.objects.all()
    serializer_class=SeriesSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer

    @action(detail=True)
    def related_reports(self,request,pk=None):
        device=Device.objects.filter(id=pk)
        if len(device)>0:
            serializer = ReportSerializer(Report.objects.filter(device=device[0]),many=True)
            return Response(serializer.data)
        else:
            return Response([])

class ReportViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
