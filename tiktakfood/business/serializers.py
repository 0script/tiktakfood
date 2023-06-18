from rest_framework import serializers

from .models import BusinessCategory,Business

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Product
#         fields=(
#             'id',
#             'name',
#             'get_absolute_url',
#             'description',
#             'price',
#             'get_image',
#             'get_thumbnail'
#         )

# class CategorySerializer(serializers.ModelSerializer):
#     products=ProductSerializer(many=True)

#     class Meta:
#         model=Category
#         fields=(
#             'id',
#             'name',
#             'get_absolute_url',
#             'products',
#         )

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business
        fields = (
            'name',
            'phone',
            'address',
            'logo',
            'get_image',
            'get_thumbnail',
        )
        
class BusinessCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    business = BusinessSerializer(many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'phone',
            'address',
            'get_absolute_url',
            )