from django.shortcuts import render
from rest_framework import generics
from task_2.serializers import ProductDetailSerializer
from task_2.models import Product


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()