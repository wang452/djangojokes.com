from django.urls import path

# import JokeListView from the jokes\views.py file in same directory with urls.py
from .views import (
  JokeListView, JokeDetailView, JokeCreateView, 
  JokeUpdateView, JokeDeleteView
)

# URLConf has a namespace of “jokes,” which is also the name of the app
app_name = 'jokes'

# add path to the JokeListVIew for jokes app
urlpatterns = [
  path('', JokeListView.as_view(), name='list'),

  # add path to the JokeDetailView that require pk of the joke
  # also import JokeDetailView from views.py above
  # path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
  # replace primary key <int:pk> with slug field dor detail view joke
  path('joke/<slug>/', JokeDetailView.as_view(), name='detail'),

  # add path to the JokeCreateView and JokeUpdateView required pk
  # after import them from .views
  #path('joke/<int:pk>/update/', JokeUpdateView.as_view(), name='update'),
  # replace primary key <int:pk> with slug field for update/edit joke
  path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),

  path('joke/create/', JokeCreateView.as_view(), name='create'),

  # add path to the JokeDeleteView with primary key and name = delete
  # path('joke/<int:pk>/delete/', JokeDeleteView.as_view(), name='delete'),
  # replace primary key <int:pk> with slug field for delete operation
  path('joke/<slug>/delete/', JokeDeleteView.as_view(), name='delete'),
]