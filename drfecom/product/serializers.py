from rest_framework import serializers
from .models import Brand, Category, Product

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'

class Brandserializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields = '__all__'

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = '__all__'
        
