from django.urls import path
from .views import get_network_info

urlpatterns = [
    path('planner', get_network_info, name='planner'),
]