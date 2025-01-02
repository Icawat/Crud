from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FoodCategories, FoodRecipe, Comment
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FoodCategories, FoodRecipe, Comment, Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'image', 'description', 'recipe', 'category']
    template_name = 'create_post.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['name', 'image', 'description', 'recipe', 'category']
    template_name = 'update_post.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list')


class CategoryListView(ListView):
    model = FoodCategories
    template_name = 'food_categories.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = FoodCategories
    fields = ['name', 'description']
    template_name = 'base.html'
    success_url = reverse_lazy('categories') 


class RecipeListView(ListView):
    model = FoodRecipe
    template_name = 'homepage.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = FoodRecipe
    template_name = 'view_food.html'

class RecipeCreateView(CreateView):
    model = FoodRecipe
    fields = ['name', 'image', 'description', 'recipe', 'category']
    template_name = 'base.html'
    success_url = reverse_lazy('home')


class CommentCreateView(CreateView):
    model = Comment
    fields = ['content', 'recipe']
    template_name = 'base.html'
    success_url = reverse_lazy('home')