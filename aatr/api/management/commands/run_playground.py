from django.core.management import base

from aatr.api.models import Session, User


class Command(base.BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create_user(email='jules@gmail.com')
        user = User.objects.first()
        session = Session.objects.create(user=user)
        print('session:', session)
