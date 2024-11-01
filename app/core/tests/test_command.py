"""
Test custom django management commands
"""

# to mock the behavioir of the database to simulate when db returning response or not
#  
from unittest.mock import patch

# one of the possible errors when tring to connect to db before db is ready
from psycopg2 import OperationalError as Psycopg2Error
# helper func to simulate and call the command by name. 
from django.core.management import call_command
# another error tht can be thrown by db depending of what stage it is 
from django.db.utils import OperationalError
# base test class, since we're testing if db available, we dont neeed db migrations of test db
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

        patched_check.assert_called_once_with(databases=['default'])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting Operationl error"""

        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        
        call_command("wait_for_db")

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

