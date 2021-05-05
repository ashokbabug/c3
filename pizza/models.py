from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category},{self.size}'
class Toppings(models.Model):
    topping = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.topping}'

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return f'{self.name}'


