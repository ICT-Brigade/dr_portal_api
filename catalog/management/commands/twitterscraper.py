from typing import ContextManager
from django.core.management.base import BaseCommand, CommandError

from catalog.jobs import twitter_scraper

class Command(BaseCommand):
	"""Terminal based api for twitter scraper management"""

	def add_arguments(self, parser):
		#Named (optional) arguments
		parser.add_argument(
			'--run',
			action='store_true',
			help='Run scraper',
		)

	def handle(self, *args, **options):
		try:
			if options["run"]:
				twitter_scraper.run(*args, **options)
				self.stdout.write(self.style.SUCCESS("Successfully scraped new tweets."))
				self.stdout.write(self.style.SUCCESS("Successfully loaded new tweets in database."))
		except CommandError as e:
			raise e
