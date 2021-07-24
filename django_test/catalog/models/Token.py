from django.db import models
from shared.mixins import BaseModelMixin


class Token(BaseModelMixin):
	value = models.CharField(max_length=1024)
	type = models.ForeignKey(
		'TokenType',
		on_delete=models.RESTRICT
	)
