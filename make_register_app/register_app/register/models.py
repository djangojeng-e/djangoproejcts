from django.db import models

# Create your models here.

class Django_user(models.Model): 
    username = models.CharField(max_length=64, verbose_name="사용자명")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registered_date = models.DateTimeField(auto_now=True, verbose_name="등록타임")


    class Meta:
        db_table = 'Djangojenge_user'


