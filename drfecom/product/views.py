from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import Categoryserializer,Brandserializer, Productserializer
from drf_spectacular .utils import extend_schema

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    queryset= Category.objects.all()

    @extend_schema(responses=Categoryserializer)
    def list(self,request):
        serializer = Categoryserializer(self.queryset, many=True)
        return Response(serializer.data)
'''
alternate method which gives get,post,put and delete options at a time 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer'''

class BrandViewSet(viewsets.ViewSet):
    queryset= Brand.objects.all()

    @extend_schema(responses=Brandserializer)
    def list(self,request):
        serializer = Brandserializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    queryset= Product.objects.all()

    @extend_schema(responses=Productserializer)
    def list(self,request):
        serializer = Productserializer(self.queryset, many=True)
        return Response(serializer.data)