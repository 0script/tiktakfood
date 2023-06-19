from django.contrib import admin

from .models import (
    ProductCategory,
    FoodCategory,
    Product,
    ProductFood,
)
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(FoodCategory)
admin.site.register(Product)
admin.site.register(ProductFood)