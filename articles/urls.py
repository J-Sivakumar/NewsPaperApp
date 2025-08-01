from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView, ArticleCreateView
urlpatterns = [
    path('',ArticleListView.as_view(), name= 'article_list'),
    path('<int:pk>/',ArticleDetailView.as_view(), name= 'article_detail'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name= 'article_delete'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name= 'article_edit'),
    path('new/',ArticleCreateView.as_view(), name= 'article_new'),
]