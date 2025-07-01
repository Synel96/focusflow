from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    
    #JWT Token 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login, token request
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
]