from django.views.generic import ListView
from projects.models import ArtProject, Project, ResearchProject


class ProjectList(ListView):
    model = Project
    template_name = 'projects/list.html'


class ArtProjectList(ListView):
    model = ArtProject
    template_name = 'projects/list.html'


class ResearchProjectList(ListView):
    model = ResearchProject
    template_name = 'projects/list.html'

