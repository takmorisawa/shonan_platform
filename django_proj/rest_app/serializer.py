from rest_framework import serializers
from rest_app.models import Spot,Post

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spot
        fields=("id","name","address")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=("id","comment")
