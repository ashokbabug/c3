from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id','category','toppings']
        # extra_kwargs = {'toppings':{'required':False}}