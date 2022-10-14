from rest_framework import serializers
from task_2.models import Product


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FileSerializerXLSX(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
