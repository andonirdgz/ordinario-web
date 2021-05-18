from django.urls import path
from . import views as project_views
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

project_patterns = ([
    path('', ProjectsListView.as_view(), name='projects'),
    path('<int:pk>/<slug:project_slug>', ProjectDetailView.as_view(), name='project'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProjectDeleteView.as_view(), name='delete'),

],'projects')