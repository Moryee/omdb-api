from django.core.management.base import BaseCommand, CommandError
from series.models import Question as Poll

# Це приклад з якогось туторіалу, не приймати близько до серця
class Command(BaseCommand):
    help = 'Retrieves all GOT episodes'
    url = 'http://www.omdbapi.com/?t=Game+Of+Thrones&apikey=a46d1bf5'
    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        # Це приклад з якогось туторіалу
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)
            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))