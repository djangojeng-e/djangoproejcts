from django.db import models

# Create your models here.


class Users(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날자')

    class Meta:
        db_table = 'shoppingmall_users'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'