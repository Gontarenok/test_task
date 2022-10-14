from django.shortcuts import render
from rest_framework import generics, status
from task_2.serializers import ProductDetailSerializer, FileSerializerXLSX
from task_2.models import Product
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()



# class ExampleView(APIView):
#     """
#     A view that can accept POST requests with JSON content.
#     """
#     parser_classes = [JSONParser]
#
#     def post(self, request, format=None):
#         return Response({'received data': request.data})



class FileUploadView(generics.CreateAPIView):
    """
    POST: upload file to save data in the database
    """
    parser_classes = [MultiPartParser]
    serializer_class = FileSerializerXLSX

    def post(self, request, format=None, **kwargs):
        """
        Allows to upload file and lets it be handled by pandas
        """

        serialized = FileSerializerXLSX(data=request.data)
        if serialized.is_valid():
            file_obj = request.data['file']
            # file_bytes = file_obj.read()
            print(file_obj)
            # import_excel_task.delay(file_obj)
            print("its working")
            return Response(status=204)

        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)