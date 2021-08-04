from attr import fields
from django.db import models
from django.forms.models import model_to_dict


class BaseModel(models.Model):
	def as_dict(self):
		return model_to_dict(self)

	class Meta:
		abstract = True
