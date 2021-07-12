from django.db import models
from shared.mixins import BaseModelMixin


class Post(BaseModelMixin):
	post_id = models.BigIntegerField()
	link = models.URLField(max_length=1024)
	description = models.TextField()
	campaign_type_id = models.ForeignKey(
		'CampaignType',
		on_delete=models.RESTRICT
	)
	source_account = models.CharField(max_length=50)
	image_link = models.URLField(max_length=1024, default=None)
	beneficiary_location = models.CharField(max_length=255, default=None)
	posted_at = models.DateTimeField()
	is_hidden = models.BooleanField(default=False)
