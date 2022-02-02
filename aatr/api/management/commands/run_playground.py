import base64
import os

from django.core.management import base


class Command(base.BaseCommand):

    def handle(self, *args, **options):
        print(base64.urlsafe_b64encode(s=os.urandom(64)).decode())

    def gen_token(self, byte_length: int):
        print(base64.urlsafe_b64encode(s=os.urandom(byte_length)).decode())
