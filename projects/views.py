from django.views.generic import ListView
from rest_framework import viewsets

from projects.models import ArtProject, Project, ResearchProject
from projects.serializers import ProjectPolymorphicSerializer


class ProjectList(ListView):
    model = Project
    template_name = 'projects/list.html'


class ArtProjectList(ListView):
    model = ArtProject
    template_name = 'projects/list.html'


class ResearchProjectList(ListView):
    model = ResearchProject
    template_name = 'projects/list.html'


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectPolymorphicSerializer

