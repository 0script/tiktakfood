from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
    ProductCategory,
    FoodCategory,
    Product,
    ProductFood,
)
from .serializers import ProductSerializer,ProductFoodSerializer

import requests

API_KEY1='db7bfcd23fb848ba9b98b2376182ad75'
API_URL='https://ipgeolocation.abstractapi.com/v1/?api_key='+API_KEY1

def geo_ip_location(ip):
    try:
        r = requests.get(API_URL, params={'ip_address': ip})
        return r.json()
    except requests.exceptions.RequestException as e:
        raise e

# Create your views here.


# class BusinessCategoryView(viewsets.ViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # queryset = User.objects.all().order_by('-date_joined')
#     # serializer_class = UserSerializer
#     # # permission_classes = [permissions.IsAuthenticated]
#     def get(self,request,format=None):
#         categories=BusinessCategory.objects.all()
#         serializer=CategorySerializer(products,many=True)
#         return Response(serializer.data)

class ProductView(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
        # determine client location 
        user_ip=request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip:
            ip = user_ip.split(',')[0]   
        else:
            ip = request.META.get('REMOTE_ADDR')

        # get random food near by
        # get random product near by function
        # get a random list of product by business near by
        # each one business should have 2 .. 3 product listed 
        # display based on prod ratting 
        # 

        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)