from django.shortcuts import render, redirect
from rest_app.models import Report
from rest_app.serializer import ReportSerializer
import pandas as pd
from io import TextIOWrapper, StringIO
import json


def upload(request):
    params = { "breadcrumblist" : [ ["HOME", ""] ] }

    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        df = pd.read_csv(form_data)
        json_data = df.to_json(orient="records")
        data = json.loads(json_data)
        serializer = ReportSerializer(data=data, many=True)
        if serializer.is_valid():
            params["columns"] = df.columns.get_values()
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
