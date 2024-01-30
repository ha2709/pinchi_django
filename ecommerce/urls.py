from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
 

 

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'discounts', views.DiscountViewSet)
router.register(r'shopping_cart', views.ShoppingCartViewSet)
 
# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
     path('register/', views.register_user, name='register_user'),
]
