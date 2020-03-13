from django.db import models

class Spot(models.Model):
    name=models.CharField("名称",max_length=255)
    address=models.CharField("住所",max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    spot=models.ForeignKey(Spot,verbose_name="スポット",related_name="posts",on_delete=models.CASCADE)
    comment=models.TextField("コメント",blank=True)

    def __str__(self):
        return self.comment
