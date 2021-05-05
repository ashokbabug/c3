from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import *

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if request.data['category'].lower() not in ('regular','square',):
            return Response('category should be regular or square',status=401)
        if request.data['size'] not in str(Category.objects.values_list('size')):
            return Response('size should be valid',status=401)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PizzaViewset(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
@api_view(['GET',])
def pizzaFilter(request,category,size):
    if request.method == "GET":
        try:
            category1 = Category.objects.get(category=category,size=size)
            pizza = Pizza.objects.filter(category=category1)
            serializer = PizzaSerializer(pizza,many=True)
            return Response(serializer.data,status=200)
        except:
            return Response(f"category not found")
            

@api_view(['POST',])
def categoryAdd(request):
    if request.method=='POST':
        print(request.data)
    


