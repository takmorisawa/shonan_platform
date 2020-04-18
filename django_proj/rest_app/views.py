from django.shortcuts import render
from django.db.models import Count

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

    @action(detail=True)
    def get_related_devices(self,request,pk=None):
        queryset=Device.objects.select_related("series").filter(series_id=pk)
        serializer = DeviceSerializer(queryset,many=True)
        return Response(serializer.data)

    @action(detail=True)
    def count_related_reports(self,request,pk=None):
        queryset=Report.objects.prefetch_related(
        "device__series").filter(
        device__series=pk).values(
        "device_id","usable").annotate(
        dcount=Count("device_id"))

        devices=Device.objects.filter(series_id=pk)
        ret={ device.id: {
                "device_name": device.name,
                "yes": 0,
                "no": 0 }
              for device in devices }

        for query in queryset:
            ret[query["device_id"]]["yes" if query["usable"] else "no"]=query["dcount"]

        return Response(ret.values())


class DeviceViewSet(viewsets.ModelViewSet):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer

    @action(detail=True)
    def get_related_comments(self,request,pk=None):
        queryset=Report.objects.select_related("device").filter(device_id=pk)

        ret={ "yes":[], "no":[] }

        for query in queryset:
            ret["yes" if query.usable else "no"].append(
                {
                    "user_id": query.user_id,
                    "date": query.date,
                    "comment": query.comment })

        return Response(ret)


class ReportViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
