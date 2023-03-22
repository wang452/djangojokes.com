from django.urls import path

# import JokeListView from the jokes\views.py file in same directory with urls.py
from .views import JokeListView, JokeDetailView

# URLConf has a namespace of “jokes,” which is also the name of the app
app_name = 'jokes'

# add path to the JokeListVIew for jokes app
urlpatterns = [
  path('', JokeListView.as_view(), name='list'),

  # add path to the JokeDetailView that require pk of the joke
  # also import JokeDetailView from views.py above
  path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
]