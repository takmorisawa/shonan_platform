from django.shortcuts import render
from django.db.models import Count
from django.utils.html import escape

import django_filters
from rest_framework import viewsets,filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

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
        devices=Device.objects.filter(series_id=pk)
        ret={ device.id: {
                "device_id": device.id,
                "device_name": device.name,
                "yes": 0,
                "no": 0,
                "all": 0,
                "voice_only": 0,
                "data_only": 0,
                "none": 0}
              for device in devices }

        queryset=Report.objects.prefetch_related(
        "device__series").filter(
        device__series=pk,authorized=True)

        usableset=queryset.values(
        "device_id","usable").annotate(
        dcount=Count("device_id"))

        specset=queryset.values(
        "device_id","voice","data").annotate(
        dcount=Count("device_id"))

        for query in usableset:
            ret[query["device_id"]]["yes" if query["usable"] else "no"]=query["dcount"]

        for query in specset:
            device_id=query["device_id"]
            dcount=query["dcount"]
            if query["voice"]==Report.AVAILABLE:
                key="all" if query["data"]==Report.AVAILABLE else "voice_only"
                ret[device_id][key]+=dcount
            else:
                key="data_only" if query["data"]==Report.AVAILABLE else "none"
                ret[device_id][key]+=dcount

        return Response(ret.values())


class DeviceViewSet(viewsets.ModelViewSet):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer

    # @action(detail=True)
    # def get_related_comments(self,request,pk=None):
    #     queryset=Report.objects.select_related("device").filter(device_id=pk)
    #
    #     ret={ "yes":[], "no":[] }
    #
    #     for query in queryset:
    #         ret["yes" if query.usable else "no"].append(
    #             {
    #                 "user_id": query.user_id,
    #                 "date": query.date,
    #                 "comment": escape(query.comment) if query.enable_escape else query.comment })
    #
    #     return Response(ret)


class ReportViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["user_id","date","usable","comment","enable_escape","authorized","device","product"]


    def list(self,request):
        queryset = ReportViewSet.queryset

        query_dict = { k:v[0].split(",") for k,v in dict(request.query_params).items()}
        query_dict = {
            k if len(v)==1 else k + "__in"
            : v[0] if len(v)==1 else v
            for k,v in query_dict.items() }
        queryset = queryset.filter(**query_dict).order_by("-priority")

        serializer = ReportSerializer(queryset,many=True)
        for item in [item for item in serializer.data if item["enable_escape"]]:
            item["comment"]=escape(item["comment"])
        return Response(serializer.data)


    # def get_queryset(self):
    #     queryset = Report.objects.all()
    #     value = request.query_params.get('authorized',None)
    #     if value is not None:
    #         queryset = queryset.filter(authorized=value)
    #     return queryset
