from rest_framework import generics
from .models import Cryptocurrency, Dolarhoy
from .serializers import CryptocurrencySerializer, DolarhoySerializer
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# class CryptoViewSet(viewsets.ReadOnlyModelViewSet): # new
#     permission_classes = (AllowAny,)
#     queryset = Cryptocurrency.objects.all()
#     serializer_class = CryptocurrencySerializer


class CryptoViewSet(viewsets.ReadOnlyModelViewSet): # new
    permission_classes = (AllowAny,)
    serializer_class = CryptocurrencySerializer
    
    def get_queryset(self):
        cryptos = Cryptocurrency.objects.all()
        return cryptos

    def retrieve(self, request, *args, **kwargs):  # agregar parametros a la busqueda url
        params = kwargs
        print(params['pk'])
        params_list = params['pk'].split('-')
        cryptos = Cryptocurrency.objects.filter(cryptocurrency_subtitle=params_list[0], cryptocurrency_name=params_list[1])
        serializer = CryptocurrencySerializer(cryptos, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, kwargs):  # dar mensaje a la hora de eliminar
        logedin_user = request.user
        if(logedin_user == 'admin'):
            crypto = self.get_object()
            crypto.delete()
            reponse_message={'message': 'Destroy from CryptoViewSet succed: Item deleted'}
        else:
            response_message={'message': 'Destroy from CryptoViewSet failed: User is not admin'}




class DolarViewSet(viewsets.ReadOnlyModelViewSet): # new
    permission_classes = (AllowAny,)
    queryset = Dolarhoy.objects.all()
    serializer_class = DolarhoySerializer