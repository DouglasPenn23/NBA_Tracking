from django.urls import path
from .views import player_availability

urlpatterns = [
    path('availability/', player_availability, name='player_availability'),
]
