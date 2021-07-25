from attr import fields
from django.db import models


class BaseModel(models.Model):
	def as_dict(self):
		fields = [f.name for f in self._meta.get_fields()]
		return {k:v for k, v in vars(self).items() if k in fields}

	class Meta:
		abstract = True
