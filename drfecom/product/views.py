from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import Categoryserializer
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