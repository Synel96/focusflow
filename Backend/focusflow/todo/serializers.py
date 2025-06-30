from .models import Users
from .models import Categories
from .models import Todos

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = Users
        fields = ['id', 'email', 'user_name', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'required': True},
            'user_name': {'required': True},
            'first_name': {'required': False, 'allow_blank': True},
            'last_name': {'required': False, 'allow_blank': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
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
