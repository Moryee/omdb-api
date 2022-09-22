from django.core.management.base import BaseCommand, CommandError
from series.tasks import retrieve_episodes


class Command(BaseCommand):
    help = 'Retrieves all GOT episodes'

    def handle(self, *args, **options):
        retrieve_episodes.delay()
