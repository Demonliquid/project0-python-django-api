from rest_framework import generics
from .models import Cryptocurrency, Dolarhoy
from .serializers import CryptocurrencySerializer, DolarhoySerializer
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CryptoViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CryptocurrencySerializer

    def get_queryset(self):  # BASIC
        cryptos = Cryptocurrency.objects.all()
        return cryptos

    def retrieve(self, request, *args, **kwargs):  # Usar parametros en el URL
        params = kwargs
        print(params['pk'])
        # MULTIPLE PARAMTERS
        params_list = params['pk'].split('-')
        cryptos = Cryptocurrency.objects.filter(cryptocurrency_subtitle=params_list[0], cryptocurrency_name=params_list[1])
        serializer = CryptocurrencySerializer(cryptos, many=True)
        return Response(serializer.data)
