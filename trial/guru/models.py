from django.db import models

# Create your models here.
class db(models.Model):
	id=models.AutoField(primary_key=True)
	Mname=models.CharField(max_length=20)
	Mphno=models.CharField(max_length=10)
	Mpassword=models.CharField(max_length=12)
	Mprof=models.CharField(max_length=12,default="student",null=False)
	Memail=models.EmailField(max_length=30)

class assign(models.Model):
	id=models.AutoField(primary_key=True)
	Topic=models.CharField(max_length=50)
	Assignment=models.CharField(max_length=200)