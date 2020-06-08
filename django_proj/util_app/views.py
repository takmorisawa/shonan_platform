from django.shortcuts import render, redirect
from rest_app.models import Report, Device
from rest_app.serializer import ReportSerializer, DeviceSerializer
from io import TextIOWrapper, StringIO
import json
import csv


def upload(request, serializer_class, model_class):
    params = { "breadcrumblist" : [ ["HOME", "/util/upload/"] ] }

    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')

        reader = csv.reader(form_data)
        header = next(reader)
        tmp_data = []
        for row in reader:
            tmp_data.append({k:v for k,v in zip(header, row)})
        json_data = json.dumps(tmp_data)

        data = json.loads(json_data)
        serializer = serializer_class(data=data, many=True)
        if serializer.is_valid():
            params["records"] = data
            params["json"] = json_data
        else:
            params["message"] = "不正な入力ファイルです"

    elif "json" in request.POST:
        serializer = serializer_class(data=json.loads(request.POST["json"]), many=True)
        if serializer.is_valid():
            for data in serializer.validated_data:
                obj = model_class.objects.create(**data)
            params["message"] = "アップロード完了"
        else:
            params["message"] = "アップロードに失敗しました"

    if "json" in params:
        params["breadcrumblist"].append(["データチェック", ""])
    else:
        params["disabled"] = "disabled"

    return params

def upload_report(request):
    params = upload(request, ReportSerializer, Report)
    params["breadcrumblist"].insert(1,["Report", ""]);
    return render(request, 'upload.html', params)

def upload_device(request):
    params = upload(request, DeviceSerializer, Device)
    params["breadcrumblist"].insert(1,["Device", ""]);
    return render(request, 'upload.html', params)

def upload_top(request):
    params = {
        "breadcrumblist" : [ ["HOME", ""] ],
        "tables" : [ ["Device", "./device"], ["Report", "./report"] ] }
    return render(request, 'upload_top.html', params)
