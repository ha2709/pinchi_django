from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,ProductViewSet
# ,OrderViewSet,DiscountViewSet
from .views.user_view import UserViewSet
from .views.login import *


# Create a router and register our viewsets with it
router = DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)
# router.register(r'orders', views.OrderViewSet)
# router.register(r'discounts', views.DiscountViewSet)
# router.register(r'shopping_cart', views.ShoppingCartViewSet)
# router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
    #  path('register/', views.register_user, name='register_user'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('users/', CreateUserView.as_view()),
    # path('users/verify/<str:token>/', VerifyUserView.as_view()),
    # # path('users/register/', RegisterUserView.as_view()),
    path('register/', RegisterUserView.as_view(), name='register_customer'),
]
