"""djangojokes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# add import include to define path to the app URLConf file
from django.urls import path, include

urlpatterns = [
    # add path to django admin documentation generator urls
    # must add admin/doc path before teh admin path pattern
    # Admin
    path("admin/doc/", include('django.contrib.admindocs.urls')),
    path("admin/", admin.site.urls),

    # User Management
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),

    # Local Apps
    # add path of the URLConf file for pages app
    path('', include('pages.urls')),

    # 2nd - add path to the URLConf file of jokes app
    path('jokes/', include('jokes.urls')),

    # 3rd - add path to the URLConf file of jobs app
    path('jobs/', include('jobs.urls')),
]
