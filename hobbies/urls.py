from django.urls import path
from . import views as hobby_views
from .views import HobbiesListView, HobbyCreateView, HobbyUpdateView, HobbyDeleteView

hobby_patterns = ([
    path('', HobbiesListView.as_view(), name='hobbies'),
    path('create/', HobbyCreateView.as_view(), name='create'),
    path('update/<int:pk>', HobbyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', HobbyDeleteView.as_view(), name='delete'),

],'hobbies')
