from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
from django.shortcuts import redirect

def homepage_redirect(request):
    return redirect('/api/')


def homepage(request):
    return HttpResponse("Welcome to the homepage!")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
