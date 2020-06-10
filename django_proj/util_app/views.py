from django.shortcuts import render, redirect
from rest_app.models import Report, Device
from rest_app.serializer import ReportSerializer, DeviceSerializer
from io import TextIOWrapper, StringIO
import json
import csv
import re


class Meta(type):
    def __init__(cls, name, bases, attribute):
        super(Meta, cls).__init__(name, bases, attribute)
        validate_detail = getattr(cls, "validate_detail")
        upload_detail = getattr(cls, "upload_detail")
        serializer_class = getattr(cls, "serializer_class")
        model_class = getattr(cls, "model_class")
        cls.validate = lambda request: validate_detail(request, serializer_class)
        cls.upload = lambda request : upload_detail(request, serializer_class, model_class)


class CsvUploadViewSet(metaclass=Meta):
    serializer_class = None
    model_class = None

    def validate_detail(request, serializer_class):

        path = request.path
        m = re.match("/util/upload/([^/]+)/.*", path)
        target = m.groups()[0] if m else ""

        params = {
            "breadcrumblist" : [ ["HOME", "/util/upload/"], [target.capitalize(), ""] ],
            "validate_action" : re.sub("process/.*","", path),
            "upload_action" : "./process/",
            "message" : "",
        }
        if "success" in path:
            params["message"] = "アップロード成功"
        elif "fail" in path:
            params["message"] = "アップロード失敗"

        if 'csv' in request.FILES:
            form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')

            # get json string
            reader = csv.reader(form_data)
            header = next(reader)
            tmp_data = []
            for row in reader:
                tmp_data.append({k:v for k,v in zip(header, row)})
            json_data = json.dumps(tmp_data)

            # get dictionary and serialize
            data = json.loads(json_data)
            serializer = serializer_class(data=data, many=True)
            if serializer.is_valid():
                params["records"] = data
                params["json"] = json_data
            else:
                params["message"] = "不正な入力ファイルです"

        if "json" in params:
            params["breadcrumblist"].append(["データチェック", ""])
        else:
            params["disabled"] = "disabled"

        return render(request, 'upload.html', params)


    def upload_detail(request, serializer_class, model_class):

        url = "./fail/"
        if "json" in request.POST:
            serializer = serializer_class(data=json.loads(request.POST["json"]), many=True)
            if serializer.is_valid():
                for data in serializer.validated_data:
                    obj = model_class.objects.create(**data)
                url = "./success/"

        return redirect(url)


class DeviceUploadViewSet(CsvUploadViewSet):
    serializer_class = DeviceSerializer
    model_class = Device


class ReportUploadViewSet(CsvUploadViewSet):
    serializer_class = ReportSerializer
    model_class = Report


def upload_top(request):
    params = {
        "breadcrumblist" : [ ["HOME", ""] ],
        "tables" : [ ["Device", "./device"], ["Report", "./report"] ] }
    return render(request, 'upload_top.html', params)
