from rest_framework import serializers
from .models import Cryptocurrency

class CryptocurrencySerializer(serializers.ModelSerializer):
	class Meta:
		model = Cryptocurrency
		fields = ['cryptocurrency_name', 'cryptocurrency_subtitle', 'price', 'market_number', 'market_unit', 'change']