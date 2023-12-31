from django.utils.text import slugify

from rest_framework import serializers
from decimal import Decimal

from .models import Category, Product

class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title', 'unit_price', 'unit_price_after_tax',
         'category', 'inventory', 'description']
    
    title = serializers.CharField(max_length=255, source='name')
    unit_price_after_tax = serializers.SerializerMethodField()
    
    def get_unit_price_after_tax(self, product):
        return round(product.unit_price * Decimal(1.09), 2)

    def validate(self, data):
        if len(data['name'])<=6:
            raise serializers.ValidationError('Product title length should be at least 6')
        return data

    def create(self, validated_data):
        product = Product(**validated_data)
        product.slug = slugify(product.name)
        product.save()
        return product
        