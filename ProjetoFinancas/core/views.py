from django.shortcuts import get_object_or_404, render
from .models  import Project
from django.views.generic import CreateView
# Create your views here.
def project_list(request):
    return render(request, 'project-list.html')

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project-detail.html', {'project':project, 'expense_list': project.expenses.all()})


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'add-project.html'
    fields = ('name', 'budget', )