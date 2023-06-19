from rest_framework import serializers

from .models import BusinessCategory,Business

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