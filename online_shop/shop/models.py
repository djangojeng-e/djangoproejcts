from django.db import models

# Create your models here.

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # Defines Category Name
    meta_description = models.TextField(blank=True)         # For SEO purposes

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    # Creates URL as per names
    # allow_unicode allows to use other language values other than english.
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])

