"""
Test custom django management commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

# using simpletest case since we're simulating db behavior and no need for migrations 

# patch mocks behavior of db
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db is ready
        i,e continue with application"""
        patched_check.returned_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])