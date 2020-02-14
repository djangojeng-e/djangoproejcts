from django.db import models

# Create your models here.
from django.urls import reverse

# Shop app manages product. Product and Category are set
# Each product belongs to many category.
# one-to-many relationship


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
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_length=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

