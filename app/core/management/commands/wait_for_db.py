"""
        Django command to wait for the database connetion, untill they is available
    """

import time
from psycopg2 import OperationalError as Psycopg2OpErr
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database 

    Args:
        BaseCommand ([type]): [description]
    """

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for the database....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True

            except (Psycopg2OpErr, OperationalError):
                self.stdout.write('Database unavailable, pleace wait .....')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database ready!'))
