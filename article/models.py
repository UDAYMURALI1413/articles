from django.db import models
from django.utils import timezone

class Article(models.Model):
    CATEGORY_CHOICES=[
        ('programming','programming'),('News','News'),('IT','IT'),('Science','Science'),('Health','Health'),
    ]

    Title= models.CharField(max_length=300,unique=True)
    content = models.TextField()
    author = models.CharField(max_length=200)
    created = models.DateTimeField(default = timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    article_cost = models.IntegerField(default=0.0)
    article_category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    
    
    def __str__(self):
        return self.Title
# Create your models here.
