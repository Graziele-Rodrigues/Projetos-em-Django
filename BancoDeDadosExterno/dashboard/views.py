from django.shortcuts import render
from .models import Estudantes
# Create your views here.
def index(request):
    estudantes = Estudantes.objects.all()
    context = {
        'estudantes': estudantes
    }
    return render(request, 'index.html', context)