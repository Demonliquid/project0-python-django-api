from rest_framework import generics
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CryptoViewSet(viewsets.ModelViewSet): # new
    permission_classes = IsAuthenticated
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer