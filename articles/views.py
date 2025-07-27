from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
    context_object_name = 'article'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'author')
    template_name = 'article_new.html'
    # context_object_name = 'article'