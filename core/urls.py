from django.urls import path
from . import views as core_views
from .views import HomeView, AboutView, ContactView

core_patterns = [
    path('', HomeView.as_view(), name='home'),
    path('acerca-de/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]