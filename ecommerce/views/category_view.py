from rest_framework import viewsets,  permissions
 
from ..serializers 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer