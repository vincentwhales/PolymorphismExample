
from django.urls import path

from projects import views

app_name = 'projects'

urlpatterns = [
    path('',
         views.ProjectList.as_view(), name='projects-list-all'),
    path('art',
         views.ArtProjectList.as_view(), name='projects-list-art'),
    path('research',
         views.ResearchProjectList.as_view(), name='projects-list-research'),
]
