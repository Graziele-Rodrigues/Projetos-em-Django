from django.db import models 

# Create your models here.

class Article(models.Model): 
    title = models.CharField(max_length=100) 
    autor = models.CharField(max_length=100)
    body = models.TextField() 
    date = models.DateTimeField(auto_now_add=True) 
    thumb = models.ImageField(blank=True)

    def __str__(self): 
        return self.title