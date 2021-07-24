from django.db import models
from shared.mixins import BaseModelMixin


class TokenType(BaseModelMixin):
	value = models.CharField(max_length=100, unique=True)
