from django.urls import path

from .views import api
from .views import catalog

urlpatterns = [
	path('api/campaigns/', api.campaign.get_campaigns),
	path('api/campaigns/<campaign_id>', api.campaign.get_campaign_by_id),
	path('list', catalog.PostListView.as_view(), name='post-list')
]
