from django.db import models
from shared.mixins import BaseModelMixin


class TokenType(BaseModelMixin):
	value = models.CharField(primary_key=True, max_length=100)
