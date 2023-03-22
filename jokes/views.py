from django.shortcuts import render

# Create JokeListView views for listing jokes in jokes app

from django.views.generic import ListView
from .models import Joke

class JokeListView(ListView):
    model = Joke
