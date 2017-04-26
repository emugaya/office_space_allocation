import unittest
from myapp.dojo.models.dojo import Dojo

class TestPrintRoom(unittest.TestCase):

    def test_print_room_successfully(self):


    def test_print_unavilable_room(self):
        assertEqual(print_room('Kampala'),'Room doesn\t exist', msg="Does not print none existing rooms")
