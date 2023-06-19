from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import BusinessCategory,Business
from .serializers import ProductSerializer,ProductFoodSerializer

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
        queryset = Business.objects.all()
        serializer = BusinessSerializer(queryset, many=True)
        return Response(serializer.data)