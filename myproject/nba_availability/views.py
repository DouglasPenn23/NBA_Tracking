from django.shortcuts import render
from .models import NBAPlayer


# Create your views here.
def player_availability(request):
    players = NBAPlayer.objects.all()
    return render(request, 'player_availability.html', {'players': players})
