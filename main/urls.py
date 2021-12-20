"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include

# Initialize environment variables
import environ
env = environ.Env()
environ.Env.read_env() # override env variables from .env file

# Admin page moved to an environment variable
admin_page = env('ADMIN_PAGE')
if not admin_page.endswith('/'):
    admin_page += '/'

# Basic URL Routes
urlpatterns = [
    path(admin_page, admin.site.urls),
    path('catalog/', include('catalog.urls')) # includes all url routes from the catalog section
]

# Add URL maps to redirect the base URL to the main catalog listing page
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/list', permanent=True))
]
