from rest_framework import serializers
from ecommerce.models.verificaiton_token import VerificationToken

class VerificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationToken
        fields = '__all__'