from django.urls import path 
from . import views

urlpatterns = [
    path('',views.welcome),
    # http://127.0.0.1:8000/create_articles/books/art/uday/programming/500/False/
    path('create_articles/<str:Title>/<str:content>/<str:author>/<str:article_category>/<int:article_cost>/<str:status>/', views.create_article,name='create_article'),
    path('article/', views.display_articles, name='display_articles'),
    path('remove_article/<int:article_id>/', views.remove_article, name='remove_article'),
    path('update_article/<str:Title>/<str:content>/<str:status>/', views.update_article, name='update_article'),
    path('search_article/<str:Title>/<str:status>/', views.search_article, name='search_article'),
]