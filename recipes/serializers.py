from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Recipe
from foodie_app.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class RecipeReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    favorited_by = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Recipe
        fields = ["id", "name", "description", "ingredients", "date_added", "category", "user", "image", "favorited_by"]
        read_only_fields = ['image']
        
class RecipeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "name", "description", "ingredients", "date_added", "category", "user", "image", "favorited_by"]

