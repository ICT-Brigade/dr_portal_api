from django.core.exceptions import ObjectDoesNotExist

from catalog.models import Setting, Post, Token
from scraper.scraper import scraper
from shared import obj_utils
from shared.db.BulkCreateManager import BulkCreateManager


def run(*args, **kwargs):
	try:
		options = construct_options()
		raw_campaigns = scraper.get_tweets(**options)
		valid_campaigns = clean_campaigns(raw_campaigns)
		return create_campaigns(valid_campaigns)
	except Exception as e:
		raise e


def construct_options():
	from_date = None
	to_date = None
	limit = None

	try:
		from_date = Setting.objects.get(key="from_date")
		to_date = Setting.objects.get(key="to_date")
		limit = Setting.objects.get(key="limit")
	except ObjectDoesNotExist as e:
		pass

	query = get_query()

	return {
		'from_date': from_date.value if from_date else None,
		'to_date': to_date.value if to_date else None,
		'hashtags': query,
		'limit': limit.value if limit else None
	}


def get_query():
	tokens = Token.objects.all()
	if not tokens:
		raise Exception(
			"Unable to perform scraping, keywords and tags are not set."
		)

	return construct_query(list(tokens))


def construct_query(tokens):
	tokens_copy = tokens
	hashtags = []

	for idx, token in enumerate(tokens_copy, start=0):
		if token.type_id.upper() == "TAG":
			hashtags.append(token.value)
			tokens_copy.pop(idx)

	query = " ".join(hashtags)
	query += " "
	query += " OR ".join([token.value for token in tokens_copy])

	return query


def create_campaigns(raw_campaigns):
	bulk_mgr = BulkCreateManager(chunk_size=100)

	for campaign in raw_campaigns:
		bulk_mgr.add(campaign)

	bulk_mgr.done()
	return raw_campaigns


def clean_campaigns(raw_campaigns):
	duplicates = Post.objects.filter(
		post_id__in=[campaign.get("id") for campaign in raw_campaigns]
	)

	post_map = obj_utils.as_map(duplicates, "post_id")
	posts = []
	for campaign in raw_campaigns:
		is_in_db = campaign.get("id") in post_map
		if is_in_db: continue

		posts.append(
			Post(
				post_id=campaign.get("id"),
				link=campaign.get("link"),
				description=campaign.get("tweet"),
				source_account=campaign.get("username"),
				image_link=campaign.get("thumbnail"),
				posted_at=campaign.get("date")
			))

	return posts
