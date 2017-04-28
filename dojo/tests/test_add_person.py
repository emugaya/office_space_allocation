import unittest
from myapp.dojo.models.dojo import *
from myapp.dojo.models.person import *
from myapp.dojo.models.room import *

class TestAddPersonRoom(unittest.TestCase):
    """
    This Object is used to define and run methods that check whether fuctionality of the add_person method in the Dojo.
    Testing for the allocation of room is being done using another test file test_allocate_room.py
    """

    def test_add_person_succesfully(self):
        """
        This Test Case is to check whether persons are succesfully created or added in the Dojo.
        """
        my_dojo = Dojo()
        initial_person_count = 0
        blue_office = my_dojo.create_room('office', 'blue')
        white_room = my_dojo.create_room('Office','White')
        yellow_room = my_dojo.create_room('Office','Yellow')
        add_elvis = my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        add_ezekiel = my_dojo.add_person('1002','Mugaya','Ezekiel','Fellow','N')
        new_person_count = len(my_dojo.persons)
        self.assertEqual(new_person_count - initial_person_count, 2,
                        msg="Persons have been created in the dojo successfully")

    def test_adding_existing_person_or_person_id(self):
        """
        This test case is used to ensure that the future of not adding
        the same person more than once in the dojo is avoided.
        """
        my_dojo = Dojo()
        initial_person_count = 0
        blue_office = my_dojo.create_room('office', 'blue')
        brown_living_space = my_dojo.create_room('LivingSpace', 'Brown')
        my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        new_person_count = len(my_dojo.persons)
        self.assertEqual(new_person_count - initial_person_count, 1, "Existing persons are readded to the Dojo")

    def test_adding_person_with_invalid_person_type(self):
        """
        This test case is sed to ensure that we can only add people who are either Staff or Fellows to the Dojo.
        """
        my_dojo = Dojo()
        initial_person_count = 0
        my_dojo.create_room('office', 'blue')
        chef = (my_dojo.add_person('1001','Mulinde','Elvis','Chef'))
        new_person_count = len(my_dojo.persons)
        self.assertEqual(new_person_count - initial_person_count, 0,
                        msg ='Invalid Person types are not added')
