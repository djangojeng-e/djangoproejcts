from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    # db_index = True 카테고리 정보가 저장되는 테이블은 이 이름열을 인덱스로 설정
    meta_description = models.TextField(blank=True)
    # SEO Search 를 위해 만드는 필드
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    # Category name 으로 URL을 만드는 방식 -> helps you to do SEO

    class Meta:
        ordering = ['name']
        verbose_name = 'category'           # 관리자 화면에서 객체가 단수일때 보여지는 값
        verbose_name_plural = 'categories'  # 관리자 화면에서 객체가 복수일때 보여지는 값

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    pass
