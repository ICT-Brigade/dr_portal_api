from django.db import models
from shared.mixins import BaseModelMixin


class CampaignType(BaseModelMixin):
	value = models.CharField(primary_key=True, max_length=1024)
