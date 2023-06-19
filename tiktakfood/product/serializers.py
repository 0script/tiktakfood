from rest_framework import serializers

from .models import (
    ProductCategory,
    FoodCategory,
    Product,
    ProductFood
)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'available',
            'get_image',
            'get_thumbnail',
        )

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    products = ProductSerializer(many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'products',
            )

class ProductFoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'available',
            'get_image',
            'get_thumbnail',
        )


class FoodCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    foods = ProductFoodSerializer(many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'foods',
            )