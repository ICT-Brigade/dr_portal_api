from django.db import models
from shared.mixins import BaseModelMixin


class Tag(BaseModelMixin):
	value = models.CharField(max_length=1024, unique=True)
