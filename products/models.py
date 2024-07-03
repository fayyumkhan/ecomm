from django.db import models
from base.models import BaseModel
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_images = models.ImageField(upload_to="categories")


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products")
    product_description = models.TextField()
    price = models.IntegerField(default=0)

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="images")
    images = models.ImageField(upload_to="products")    