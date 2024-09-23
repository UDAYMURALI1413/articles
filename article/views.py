from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def welcome(request):
    return HttpResponse('welcome to the app')

def create_article(request, Title, content, author, article_category, article_cost, status):
    try:
        status = status.lower() == 'true'
        article = Article(Title=Title, content=content, author=author, article_category=article_category, article_cost=article_cost, status=status)
        article.full_clean()  # Validate fields
        article.save()
        return HttpResponse(f"New Article: '{Title}' added to the system successfully...")
    except Exception as e:
        return HttpResponse(str(e))

def display_articles(request):
    articles = Article.objects.all()
    if not articles:
        return HttpResponse("No More articles are available.")
    response = "<br/>".join([f"{article.id}: {article.Title} - {article.status}" for article in articles])
    return HttpResponse(response)

def remove_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.delete()
        return HttpResponse(f"Article with Id: '{article_id}' removed from the system successfully...")
    except Article.DoesNotExist:
        return HttpResponse("Article does not exist.")

def update_article(request, Title, content, status):
    try:
        article = Article.objects.get(Title=Title)
        article.content = content
        article.status = status.lower() == 'true'
        article.save()
        return HttpResponse(f"Article: '{Title}' Updated successfully...")
    except Article.DoesNotExist:
        return HttpResponse("Article does not exist.")

def search_article(request, Title, status):
    status = status.lower() == 'true'
    articles = Article.objects.filter(Title=Title, status=status)
    if not articles:
        return HttpResponse("No articles found.")
    response = "<br/>".join([f"{article.id}: {article.Title} - {article.status}" for article in articles])
    return HttpResponse(response)
# Create your views here.
