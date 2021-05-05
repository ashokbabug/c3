from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'category', CategoryViewset)
router.register(r'pizza', PizzaViewset)

urlpatterns = [
   path(r'',include(router.urls)),
   path('pizza/filter/<str:category>/<str:size>/',pizzaFilter)
]
