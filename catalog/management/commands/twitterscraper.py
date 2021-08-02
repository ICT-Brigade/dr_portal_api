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
				data = twitter_scraper.run(*args, **options)
				self.show_messsage(len(data))
		except CommandError as e:
			raise e

	def show_messsage(self, count):
		if count:
			self.stdout.write(
				self.style.SUCCESS(
					f"Successfully scraped {count} new tweet(s)."
				)
			)
			self.stdout.write(
				self.style.SUCCESS(
					f"Successfully loaded {count} new tweet(s) in database."
				)
			)
		else:
			self.stdout.write(
				self.style.SUCCESS("No new tweets as of the moment.")
			)
