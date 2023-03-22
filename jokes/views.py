from django.shortcuts import render

# Create JokeListView view for listing jokes in jokes app

from django.views.generic import DetailView, ListView
from .models import Joke

class JokeListView(ListView):
    model = Joke

# Create JokeDetailView for jokes app to display detail of joke
# after add import DetailView above
class JokeDetailView(DetailView):
    model = Joke
