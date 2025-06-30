from django.urls import path,include
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet,TodosViewSet

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'todos', TodosViewSet, basename='todos')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    #JWT Token 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login, token request
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
    path('', include(router.urls)), 
]