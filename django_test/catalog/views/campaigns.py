import traceback, json
from attr import fields
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers

from jsonschema import FormatChecker

from catalog.models import Post
from scraper.scraper import scraper
from catalog.schemas.campaigns import CAMPAIGN_QS

from shared import obj_utils
from shared.schema_validator import (
	get_validator
)


def get_campaigns(request):
	errors = []
	try:
		validate = get_validator(CAMPAIGN_QS)
		qs = request.GET.dict()

		errors = validate(
			data=obj_utils.keys_to_number(qs, "limit", to_int=True),
			format_checker=FormatChecker()
		)
		if errors:
			raise ValidationError("schema validation error")

		campaigns = Post.objects.all()
		data = {
			"success": True,
			"data": [c.as_dict() for c in campaigns],
			"page_info": {
				"total_count": len(campaigns)
			}
		}
		return JsonResponse(data, safe=False)
	except Exception as e:
		traceback.print_exc()
		return JsonResponse({
				"success": False,
				"context": e.__class__.__name__,
				"message": str(e.args[0] if len(e.args) else e),
				"errors": errors
			},
			safe=False,
			status=417
		)
