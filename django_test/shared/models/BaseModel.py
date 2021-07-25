from attr import fields
from django.db import models
import uuid


class BaseModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	def as_dict(self):
		fields = [f.name for f in self._meta.get_fields()]
		return {k:v for k, v in vars(self).items() if k in fields}

	class Meta:
		abstract = True
