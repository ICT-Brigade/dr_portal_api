import os

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from catalog import seed


class Command(BaseCommand):
	def handle(self, *args, **options):
		try:
			seeders = sorted([
				seeder for seeder in os.listdir(os.path.dirname(seed.__file__)) \
					if not seeder.startswith("_")
				])
			for seeder in seeders:
				call_command(
					"loaddata",
					os.path.join(
						os.path.dirname(seed.__file__),
						seeder
					)
				)
		except CommandError as e:
			raise e
