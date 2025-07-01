from rest_framework import viewsets, permissions
from rest_framework import filters
from .serializers import CategoriesSerializer
from .serializers import TodosSerializer
from rest_framework import filters
from .models import Categories,Todos
    

class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
       
        return Categories.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)


class TodosViewSet(viewsets.ModelViewSet):

    serializer_class = TodosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'deadline', 'priority']
    search_fields = ['title', 'description']


    def get_queryset(self):

        return Todos.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
