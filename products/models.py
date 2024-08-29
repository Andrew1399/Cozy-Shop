from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:products_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1000, blank=True)
    slug = models.SlugField(max_length=120, db_index=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        # index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name