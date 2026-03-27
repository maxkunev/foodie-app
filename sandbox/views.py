from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import ListView, DetailView, View
from recipes.models import Recipe
from sandbox.models import Feedback
from sandbox.forms import FeedbackForm
from django.contrib import messages


def index(request):
    data = {"name": "Alberto", "age": 23}
    context = {"data": data}
    return render(request, "sandbox/index.html", context)

def about(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    return render(request, "sandbox/about.html", context)


class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/about.html"
    context_object_name = "recipes"
    
    def get_queryset(self):
        filtered_recipes = Recipe.objects.filter(category__name__icontains = "salad")
        return filtered_recipes
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "sandbox/recipe.html"
    context_object_name = "recipe"

class SpecifcRecipesView(View):
    def get(self, request, *args, **kwargs):
        refreshing_recipes = Recipe.objects.filter(description__icontains = "warm")
        context = {"refreshing":refreshing_recipes}
        return render(request, 'sandbox/refreshing_recipes.html', context) 
    

def feedback(request):
    request.session['feedback_visits'] = request.session.get('feedback_visits', 0) + 1

    
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            
            request.session['feedback_data'] = form.cleaned_data
            messages.info(request, "Confirm your submit!")
            return redirect("sandbox:feedback_review")
        
            # name = form.cleaned_data["name"]
            # email = form.cleaned_data["email"]
            # feedback = form.cleaned_data["feedback"]
            # satisfaction = form.cleaned_data["satisfaction"]
            # Feedback.objects.create(
            #     name = name,
            #     email = email,
            #     feedback = feedback,
            #     satisfaction = satisfaction
            # )
            # messages.success(request, "Feedback saved successfully!")
            # return redirect("sandbox:sandrecipes")
    else:
        form = FeedbackForm()
    context = {
                "form":form,
                "visits": request.session['feedback_visits']
               }
    return render(request, "sandbox/feedback_form.html", context)
        

def feedback_review(request):
    feedback_data = request.session.get("feedback_data", {})
    if request.method=="POST":
        Feedback.objects.create(**feedback_data)
        del request.session["feedback_data"]
        messages.success(request, "Feedback saved successfully!")
        return redirect("sandbox:sandrecipes")
    
    form = FeedbackForm(initial=feedback_data)
    
    context = {
        "form":form
    }
    
    return render(request, "sandbox/feedback_review.html", context)

def thank_you(request):
    return HttpResponse("<h1>Thank you for your feedback</h1>")
