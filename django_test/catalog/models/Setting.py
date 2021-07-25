from django.db import models
from shared.mixins import BaseModelMixin

class Setting(BaseModelMixin):
	key = models.CharField(max_length=1024, primary_key=True)
	value = models.CharField(max_length=1024)
