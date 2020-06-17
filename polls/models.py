from django.db import models

# Create your models here.
class bot1(models.Model):
    req1=models.CharField(max_length=1000)
    res1=models.CharField(max_length=1000)

class bot2(models.Model):
    req2=models.CharField(max_length=1000)
    res2=models.CharField(max_length=1000)
    
class bot3(models.Model):
    req3=models.CharField(max_length=1000)
    res3=models.CharField(max_length=1000)
    Ousestion=models.CharField(max_length=1000)


    
    