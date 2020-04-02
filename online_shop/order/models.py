from django.db import models
from shop.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


from coupon.models import Coupon

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT, related_name='order_coupon', null=True, blank=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), - MaxValueValidator(100000)])

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_product(self):
        return sum(item.get_item_price() for item in self.item.all())

    def get_total_price(self):
        total_product = self.get_total_product()
        return total_product - self.discount


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_item_price(self):
        return self.price * self.quantity

