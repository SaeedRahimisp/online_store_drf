from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        product_queryset = Product.objects.select_related('category').all()
        serializer = ProductSerializer(product_queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Ok!')

@api_view()
def product_detail(request, pk):
        product = get_object_or_404(Product.objects.select_related('category'), pk=pk)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

