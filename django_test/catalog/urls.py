from django.urls import path

from .views import campaigns

urlpatterns = [
    path('', campaigns.get_campaigns)
]
