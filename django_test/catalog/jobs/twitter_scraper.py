from django.core.exceptions import ObjectDoesNotExist

from catalog.models import Setting, Post
from scraper.scraper import scraper
from shared import db
from shared.db.BulkCreateManager import BulkCreateManager


def run(*args, **kwargs):
	try:
		options = construct_options()
		campaigns = scraper.get_tweets(**options)
		create_campaigns(campaigns)
	except Exception as e:
		raise e


def construct_options():
	from_date = None
	to_date = None
	try:
		from_date = Setting.objects.get(key="from_date")
		to_date = Setting.objects.get(key="to_date")
	except ObjectDoesNotExist as e:
		pass

	query = get_query()

	return {
		'from_date': from_date.value if from_date else None,
		'to_date': to_date.value if to_date else None,
		'hashtags': query
	}


def get_query():
	sql = """
		SELECT
			tk.id as id,
			tkt.value as type,
			tk.value as value
		FROM catalog_token tk
		LEFT JOIN catalog_tokentype tkt
		ON (
			tk.type_id = tkt.id
		);
	"""
	tokens = db.execute([[sql, None]])
	if not tokens:
		raise Exception(
			"Unable to perform scraping, keywords and tags are not set."
		)

	return construct_query(tokens)


def construct_query(tokens):
	tokens_copy = tokens
	hashtags = []

	for idx, token in enumerate(tokens_copy, start=0):
		if token.get("type").upper() == "TAG":
			 hashtags.append(token.get("value"))
			 tokens_copy.pop(idx)

	query = " ".join(hashtags)
	query += " "
	query += " OR ".join([token.get("value") for token in tokens_copy])

	return query


def create_campaigns(campaigns):
	bulk_mgr = BulkCreateManager(chunk_size=100)

	for campaign in campaigns:
		bulk_mgr.add(Post(
			post_id=campaign.get("id"),
			link=campaign.get("link"),
			description=campaign.get("tweet"),
			source_account=campaign.get("username"),
			image_link=campaign.get("thumbnail"),
			posted_at=campaign.get("date")
		))
	bulk_mgr.done()
