from django.urls import path
from . import views as artwork_views
from .views import ArtworksListView, ArtworkCreateView, ArtworkDeleteView, ArtworkUpdateView, ArtworkCreateOrder, OrderSuccess


artwork_patterns = ([
    path('', ArtworksListView.as_view(), name='artworks'),
    path('create/', ArtworkCreateView.as_view(), name='create'),
    path('update/<int:pk>', ArtworkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArtworkDeleteView.as_view(), name='delete'),
    path('order/', artwork_views.send_order, name='order_detail'),
    path('create_order/', ArtworkCreateOrder.as_view(), name='create_order'),
    path('order_success/', OrderSuccess.as_view(), name='order_success'),

], 'artworks')
