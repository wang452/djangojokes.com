from django.shortcuts import render

# import reverse_lazy function for JokeDeleteView
from django.urls import reverse_lazy

# Create JokeListView view for listing jokes in jokes app

from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)

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

# Create JokeDeleteView for jokes app to delete joke
# Use reverse_lazy function to get the data of target joke
class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

