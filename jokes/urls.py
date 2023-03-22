from django.urls import path

# import JokeListView from the jokes\views.py file in same directory with urls.py
from .views import JokeListView

# URLConf has a namespace of “jokes,” which is also the name of the app
app_name = 'jokes'

# add path to the JokeListVIew for jokes app
urlpatterns = [
  path('', JokeListView.as_view(), name='list'),
]