from rest_framework import serializers
from django.utils.html import escape
from rest_app.models import Product,Series,Device,Report,Support


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=("id","name")

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Series
        fields=("id","name")

class DeviceSerializer(serializers.ModelSerializer):
    series=serializers.PrimaryKeyRelatedField(queryset=Series.objects.all())

    class Meta:
        model=Device
        fields=("id","name","series")

class ReportSerializer(serializers.ModelSerializer):
    device=serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())
    product=serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def validate_comment(self,value):
        return value;

    class Meta:
        model=Report
        fields=("id","user_id","date","usable","comment","enable_escape",
            "authorized","priority","voice","data","device","product")

class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model=Support
        fields=("id","device_name","maker_name","voice","data","tethering","sns","product")
