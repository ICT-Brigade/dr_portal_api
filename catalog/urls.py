from django.urls import path

from .views import campaigns
from .views import catalog

urlpatterns = [
    path('', campaigns.get_campaigns),
    path('list', catalog.list)
]
