from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections
import time


class Command(BaseCommand):
    """ Custom Django command to pause execution until db availbale """
    help = 'Check if db connection established successfully '

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Waiting for DB ...'))
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections['default']
            except OperationalError:
                self.stdout.write(
                    'DB Unavailbale, waiting for 1 sec ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB Available !'))
