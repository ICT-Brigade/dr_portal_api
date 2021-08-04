import traceback

from django.http import JsonResponse

from catalog.models import Post


def get_campaigns(request):
	try:
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
				"errors": None
			},
			safe=False,
			status=417
		)


def get_campaign_by_id(request, campaign_id):
	try:
		campaign = Post.objects.filter(
				pk=campaign_id
			).select_related("campaign_type")
		data = {
			"success": True,
			"data": campaign[0].as_dict()
		}
		return JsonResponse(data, safe=False)
	except Exception as e:
		traceback.print_exc()
		return JsonResponse({
				"success": False,
				"context": e.__class__.__name__,
				"message": str(e.args[0] if len(e.args) else e),
				"errors": None
			},
			safe=False,
			status=417
		)