from django.urls import path

from projects import views

app_name = 'projects'


urlpatterns = [
    path('',
         views.ProjectList.as_view(), name='projects-list'),
]
