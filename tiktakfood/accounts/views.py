# from django.shortcuts import render

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import  Response
# from rest_framework.views import APIView
# from .utils import get_tokens_for_user

# from .serializers import RegistrationSerializer

# # Create your views here.

# class RegistrationView(APIView):
#     serializer_class = RegistrationSerializer
#     def post(self, request, *args,  **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render

from django.contrib.auth import  login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from .utils import get_tokens_for_user

from .models import CustomUser

from .serializers import RegistrationSerializer


# Create your views here.

class RegistrationView(APIView):
    def post(self, request, *args,  **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,  **kwargs):
        queryset = CustomUser.objects.all()
        serializer = RegistrationSerializer(queryset, many=True)
        return Response(serializer.data)
