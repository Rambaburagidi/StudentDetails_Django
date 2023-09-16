from django.db import models

# Create your models here.
class std(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    branch=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.BigIntegerField()


class Meta:
    db_table="std"