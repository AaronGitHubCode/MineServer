from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect, HttpResponse

from django.contrib.auth import get_user_model

from .models import *
from .forms import *

# Create your views here.
def index(request):
    current = get_user_model()

    if current is None:
        return HttpResponseRedirect('/login')
    
    context = {
        'active_players' : Player.objects.count()
    }

    return render(request, 'minecraft/index.html', context)


def player_profile(request, player_name):
    try:
        player = Player.objects.get(player_name=player_name)
    except Player.DoesNotExist as e:
        raise Http404('No se ha encontrado el jugador.')

    context = {
        'player' : player
    }

    return render(request, 'minecraft/account.html', context)


def show_worlds(request):
    context = {
        'worlds' : World.objects.all()
    }

    return render(request, 'minecraft/worlds.html', context)


def login_new_player(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = UserForm()

    context = {
        'form' : form
    }

    return render(request, 'minecraft/login.html', context)