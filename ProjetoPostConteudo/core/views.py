from django.shortcuts import render
from core.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'layout.html', {'posts': posts})


