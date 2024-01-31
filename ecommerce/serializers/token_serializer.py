from rest_framework import serializers
from ecommerce.models.token import Token

class TokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Token
        fields = ['access_token', 'token_type']
