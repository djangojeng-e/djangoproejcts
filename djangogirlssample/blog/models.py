from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
# 관계형 데이터 베이스
# 테이블끼리 관계를 가짐
# 키벨류 데이터베이스는 장점으로 속도
# RDBMS 는 시간이 좀 걸림

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True,)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
