from django.db import models
from shared.mixins import BaseModelMixin


class CampaignType(BaseModelMixin):
	value = models.CharField(max_length=1024, unique=True)
