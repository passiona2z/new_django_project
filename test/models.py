from django.db import models

# Create your models here.



# 데이터베이스 연동 작업

class Stock(models.Model): # 상속
    text = models.CharField(max_length=255, null=False)
