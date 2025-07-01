from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet,TodosViewSet

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'todos', TodosViewSet, basename='todos')


urlpatterns = [
    path('', include(router.urls)), 
]