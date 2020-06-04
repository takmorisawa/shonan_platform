from django.shortcuts import render, redirect
from rest_app.models import Report
from rest_app.serializer import ReportSerializer
from io import TextIOWrapper, StringIO
import json
import csv


def upload(request):
    params = { "breadcrumblist" : [ ["HOME", ""] ] }

    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')

        reader = csv.reader(form_data)
        header = next(reader)
        tmp_data = []
        for row in reader:
            tmp_data.append({k:v for k,v in zip(header, row)})
        json_data = json.dumps(tmp_data)

        data = json.loads(json_data)
        serializer = ReportSerializer(data=data, many=True)
        if serializer.is_valid():
            params["columns"] = header
            params["records"] = data
            params["json"] = json_data
        else:
            params["message"] = "不正な入力ファイルです"

    elif "json" in request.POST:
        serializer = ReportSerializer(data=json.loads(request.POST["json"]), many=True)
        if serializer.is_valid():
            for data in serializer.validated_data:
                report = Report.objects.create(**data)
            params["message"] = "アップロード完了"
        else:
            params["message"] = "アップロードに失敗しました"

    if "json" in params:
        params["breadcrumblist"].append(["データチェック", ""])
    else:
        params["disabled"] = "disabled"

    return render(request, 'upload.html', params)
