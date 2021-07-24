from django.db import models


class Setting(models.Model):
	key = models.CharField(max_length=1024, primary_key=True)
	value = models.CharField(max_length=1024)
