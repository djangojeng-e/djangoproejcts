from django.db import models
from fcuser.models import Fcuser
from product.models import Product
# Create your models here.


class Order(models.Model):
    fcuser = models.ForeignKey(Fcuser, on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='상품')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날자')
    quantity = models.IntegerField(verbose_name='수량')

    class Meta:
        db_table = 'fasctcampus_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'