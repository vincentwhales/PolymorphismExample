from django.views.generic import ListView

from projects.models import Project


class ProjectList(ListView):
    model = Project
    template_name = 'projects/list.html'

