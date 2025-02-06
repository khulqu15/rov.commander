from django.urls import path
from .views import get_network_info

urlpatterns = [
    path('network-select/', get_network_info, name='network-select'),
]