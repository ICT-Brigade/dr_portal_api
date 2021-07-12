from django.db import models
from shared.mixins import BaseModelMixin


class Keyword(BaseModelMixin):
	value = models.CharField(max_length=1024, unique=True)
