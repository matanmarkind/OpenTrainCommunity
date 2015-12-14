from django.core.management.base import BaseCommand, CommandError
import data.utils


class Command(BaseCommand):
    args = ''
    help = 'build services'

    def handle(self, *args, **options):
        data.utils.invalidate_cache()
        data.utils.remove_skip_stops()
        data.utils.invalidate_cache()


