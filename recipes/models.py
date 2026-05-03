from django.db import models
from django.urls import reverse
from foodie_app.models import Category
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.

class RecipeManager(models.Manager):
    def with_likes(self):
        return self.annotate(likes_total=Count('liked_by', distinct=True))

class Recipe (models.Model):
    
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    ingredients = models.TextField()
    directions = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="recipes")
    image = models.ImageField(upload_to="recipe_images/", null=True, blank=True)
    favorited_by = models.ManyToManyField(User, blank=True, related_name="favorite_recipes")
    liked_by = models.ManyToManyField(User, blank=True, related_name="liked_recipes")
    
    objects = RecipeManager()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipes:recipe_details", args=[str(self.pk)])
    
