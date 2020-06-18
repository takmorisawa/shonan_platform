from django.db import models
# from django.utils import timezone


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
    AVAILABLE = 'OK'
    UNAVAILABLE = 'NG'
    UNKNOWN = 'UK'
    AVAILABILITY_CHOICES = [
        (AVAILABLE, 'OK'),
        (UNAVAILABLE, 'NG'),
        (UNKNOWN, 'Unknown'),
    ]

    user_id=models.CharField("ユーザーID",max_length=255)
    date=models.DateField("投稿日",auto_now_add=True)
    usable=models.BooleanField("使用可否",default=False)
    comment=models.TextField("コメント")
    enable_escape=models.BooleanField("コメントのURLエンコード",default=True)
    authorized=models.BooleanField("認可",default=False)
    priority=models.IntegerField("優先度",default=100)
    voice = models.CharField("通話",max_length=2,choices=AVAILABILITY_CHOICES,default=UNKNOWN)
    data = models.CharField("データ通信",max_length=2,choices=AVAILABILITY_CHOICES,default=UNKNOWN)
    device=models.ForeignKey(Device,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
