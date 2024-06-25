from django.urls import path

from .views import *

urlpatterns = [
    path('login', login_new_player, name='login'),
    path('', index, name='index'),
    path('<str:player_name>/account', player_profile, name='account'),
    path('worlds', show_worlds, name='worlds')
]