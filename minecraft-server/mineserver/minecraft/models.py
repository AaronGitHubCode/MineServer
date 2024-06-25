from django.db import models


# Create your models here.
class World(models.Model):
    name = models.CharField(name='world_name', max_length=100)
    version = models.CharField(name='world_version', max_length=50)

    players = models.IntegerField(name='current_players')
    
    world_image = models.ImageField(name='word_image')


class Player(models.Model):
    name = models.CharField(name='player_name', max_length=100)

    player_image = models.ImageField(name='player_image')
