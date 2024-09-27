"""
Django command to wait for the database to be active
"""

from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args: Any, **options: Any):
        pass

