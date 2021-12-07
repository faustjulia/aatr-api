from django.core.management import base


class Command(base.BaseCommand):

    def handle(self, *args, **options):
        print('this is run_playgorund.py')
