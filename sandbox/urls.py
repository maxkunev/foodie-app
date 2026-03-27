from django.urls import path
from . import views


app_name = "sandbox"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name = "about"),
    path("sandrecipes/", views.RecipeListView.as_view(), name = "sandrecipes"),
    path("sandrecipes/<int:pk>/", views.RecipeDetailView.as_view(), name = "recipe_detail"),
    path("refreshing/", views.SpecifcRecipesView.as_view(), name = "refreshing_recipes"),
    path("feedback/", views.feedback, name = "feedback"),
    path("thank-you/", views.thank_you, name = "thank_you"),
    path("feedback_review/", views.feedback_review, name = "feedback_review")
]
