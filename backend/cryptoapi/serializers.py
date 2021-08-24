from rest_framework import serializers
from .models import Cryptocurrency, Dolarhoy

class CryptocurrencySerializer(serializers.ModelSerializer):
	class Meta:
		model = Cryptocurrency
		fields = ['cryptocurrency_name', 'cryptocurrency_subtitle', 'price', 'market_number', 'market_unit', 'change']

class DolarhoySerializer(serializers.ModelSerializer):
	class Meta:
		model = Dolarhoy
		fields = ['tipo_dolar', 'cotizacion_en_pesos']