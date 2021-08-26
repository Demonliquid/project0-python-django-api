from rest_framework import generics
from .models import Cryptocurrency, Dolarhoy
from .serializers import CryptocurrencySerializer, DolarhoySerializer
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CryptoViewSet(viewsets.ReadOnlyModelViewSet): # new
    permission_classes = (AllowAny,)
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

class DolarViewSet(viewsets.ReadOnlyModelViewSet): # new
    permission_classes = (AllowAny,)
    queryset = Dolarhoy.objects.all()
    serializer_class = DolarhoySerializer