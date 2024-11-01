"""
Django command to wait for the database to be active
"""

import time
from psycopg2 import OperationalError as Psycogpg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("Waiting for db....")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (OperationalError, Psycogpg2OpError):
                self.stdout.write("Database unavailable, checking in 2 second...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS('Database available'))
