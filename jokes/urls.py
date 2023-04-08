from django.urls import path

"""
from .views import (
    JokeCreateView, JokeDeleteView, JokeDetailView, JokeListView,
    JokeUpdateView
)
"""
from .views import (
  JokeListView, JokeDetailView, JokeCreateView, 
  JokeUpdateView, JokeDeleteView
)

"""
app_name = 'jokes'
urlpatterns = [
  
    # path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),
    # path('joke/<slug>/delete/', JokeDeleteView.as_view(), name='delete'),
    # path('joke/create/', JokeCreateView.as_view(), name='create'),
    # path('joke/<slug>/', JokeDetailView.as_view(), name='detail'),
    # path('', JokeListView.as_view(), name='list'),
  
    path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),
    path('joke/<slug>/delete/', JokeDeleteView.as_view(), name='delete'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
    path('joke/<slug>/', JokeDetailView.as_view(), name='detail'),
    path('', JokeListView.as_view(), name='list'),
]
"""
"""
# URLConf has a namespace of “jokes,” which is also the name of the app
app_name = 'jokes'

# add path to the JokeListVIew for jokes app
urlpatterns = [
  # add path to the JokeCreateView and JokeUpdateView required pk
  # after import them from .views
  # path('joke/<int:pk>/update/', JokeUpdateView.as_view(), name='update'),
  # replace primary key <int:pk> with slug field for update/edit joke
  path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),

  # add path to the JokeDeleteView with primary key and name = delete
  # path('joke/<int:pk>/delete/', JokeDeleteView.as_view(), name='delete'),
  # replace primary key <int:pk> with slug field for delete operationS
  path('joke/<slug>/delete/', JokeDeleteView.as_view(), name='delete'),

  path('joke/create/', JokeCreateView.as_view(), name='create'),

  # add path to the JokeDetailView that require pk of the joke
  # also import JokeDetailView from views.py above
  # path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
  # replace primary key <int:pk> with slug field dor detail view joke
  path('joke/<slug>/', JokeDetailView.as_view(), name='detail'),

  path('', JokeListView.as_view(), name='list'),
]
"""

"""The create joke is not worked with the path order below - not sure why?
  
   order path in urlpattern is matter because Django runs through each URL 
   pattern, in order, and stops at the first one that matches the requested
   URL. 

   move path of jokes/joke/create/ before the path of jokes/<slug>/ fixed
   the problem of PageNotFound to create new joke with path jokes/joke/create
   because jokes/joke/<slug> matched first before jokes/joke/create/ path 
   when try to create new joke. 

   It was worked fine until changed code to use slug in url
"""
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

  path('joke/create/', JokeCreateView.as_view(), name='create'),

  # add path to the JokeDetailView that require pk of the joke
  # also import JokeDetailView from views.py above
  # path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
  # replace primary key <int:pk> with slug field dor detail view joke
  path('joke/<slug>/', JokeDetailView.as_view(), name='detail'),

  # add path to the JokeCreateView and JokeUpdateView required pk
  # after import them from .views
  # path('joke/<int:pk>/update/', JokeUpdateView.as_view(), name='update'),
  # replace primary key <int:pk> with slug field for update/edit joke
  path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),

  # path('joke/create/', JokeCreateView.as_view(), name='create'),

  # add path to the JokeDeleteView with primary key and name = delete
  # path('joke/<int:pk>/delete/', JokeDeleteView.as_view(), name='delete'),
  # replace primary key <int:pk> with slug field for delete operation
  path('joke/<slug>/delete/', JokeDeleteView.as_view(), name='delete'),
]
