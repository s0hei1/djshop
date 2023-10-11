from django.shortcuts import render
from rest_framework import viewsets
from catalog.models import Category
from catalog.serializers.user import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.visibility()
    serializer_class = CategorySerializer
