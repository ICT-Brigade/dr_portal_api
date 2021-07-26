import uuid
from django.db import models
from shared.mixins import BaseModelMixin


class Post(BaseModelMixin):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	post_id = models.CharField(max_length=255, unique=True)
	link = models.URLField(max_length=1024)
	description = models.TextField()
	campaign_type = models.ForeignKey(
		'CampaignType',
		on_delete=models.RESTRICT,
		null=True,
		blank=True
	)
	source_account = models.CharField(max_length=50)
	image_link = models.URLField(max_length=1024, blank=True)
	beneficiary_location = models.CharField(max_length=255, blank=True)
	posted_at = models.DateTimeField()
	is_hidden = models.BooleanField(default=False)
