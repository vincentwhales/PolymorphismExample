from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('api/', include(router.urls)),
]
