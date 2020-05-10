from django.db import models
from django.utils import timezone


class Product(models.Model):
    name=models.CharField("名称",max_length=255)

    def __str__(self):
        return self.name

class Series(models.Model):
    name=models.CharField("シリーズ",max_length=255)

    def __str__(self):
        return self.name

class Device(models.Model):
    name=models.CharField("機種名",max_length=255)
    series=models.ForeignKey(Series,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Report(models.Model):
    user_id=models.CharField("ユーザーID",max_length=255)
    date=models.DateTimeField("投稿日時",default=timezone.now)
    usable=models.BooleanField("使用可否",default=False)
    comment=models.TextField("コメント")
    device=models.ForeignKey(Device,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
