from django.shortcuts import render

# Create JokeListView view for listing jokes in jokes app

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Joke

class JokeListView(ListView):
    model = Joke

# Create JokeDetailView for jokes app to display detail of joke
# after add import DetailView above
class JokeDetailView(DetailView):
    model = Joke

# Create JokeCreateView for jokes app to add new joke
class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

# Create JokeUpdateView for jokes app to update joke
class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

