from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import Article
# Create your views here. 
def index(request):
    articles = Article.objects.all() 
    return render(request, 'post.html', {'articles':articles})

def post_detail(request, id): 

    details = get_object_or_404(Article, id=id)

    return render(request, 'details.html', {'details':details})