from .models import Categories
from .models import Todos

from rest_framework import serializers



class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'user']


class TodosSerializer(serializers.ModelSerializer):
    class Meta :
        model = Todos
        fields = [
        'id',
        'title',
        'description',
        'created_at',
        'is_done',
        'category',
        'deadline',
        'priority',
        'user',
    ]
