from rest_framework import viewsets
from ..models.discount import Discount
from ..serializers.discount_serializer import DiscountSerializer
 
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

