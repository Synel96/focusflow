from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework import filters
from .serializers import UserSerializer
from .serializers import CategoriesSerializer
from .serializers import TodosSerializer
from rest_framework import filters
from .models import Categories,Todos


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
