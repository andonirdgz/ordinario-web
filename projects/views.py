from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project
from .forms import ProjectForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# def projects(request):
#     proys = Project.objects.all()
#     return render(request, 'projects/projects.html', {'projects': proys})

class ProjectsListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects:projects')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('projects:update', args=[self.object.id]) + '?ok'


class ProjectDeleteView(DeleteView):
    model = Project
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy('projects:projects')


