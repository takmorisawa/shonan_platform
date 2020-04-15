from rest_framework import serializers
from rest_app.models import Spot,Post,Report

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spot
        fields=("id","name","address")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=("id","comment")
        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields=("user_id","date","usable","comment")
