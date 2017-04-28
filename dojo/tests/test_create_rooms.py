import unittest

from myapp.dojo.models.dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    """
    This Object Tests Fuctionality of the create_room method in the dojo
    """
    def test_create_room_succesfully(self):
        """
        This test whether creating of one room is succesful
        """
        my_dojo = Dojo()
        initial_room_count = len(my_dojo.living_space) + len(my_dojo.office)
        my_dojo.create_room('office', ['Blue'])
        my_dojo.create_room('LivingSpace', ['Brown'])
        new_room_count =len(my_dojo.living_space) + len(my_dojo.office)
        self.assertEqual(new_room_count - initial_room_count,2, msg="Create Room Succesful")

    def test_for_not_creating_room_when_room_name_already_exists(self):
        """
        This Test is to make sure that rooms with the same names are not created in the dojo.
        """
        my_dojo = Dojo()
        my_dojo.create_room('office', ['blue'])
        initial_room_count = len(my_dojo.living_space) + len(my_dojo.office)
        my_dojo.create_room('office', ['blue'])
        new_room_count =len(my_dojo.living_space) + len(my_dojo.office)
        self.assertEqual(new_room_count - initial_room_count,0 ,
                        msg="Future not to create rooms with the same name succeful" )

    def test_create_invalid_room_type(self):
        """
        This test case is to ensure that only Office and LivingSpace rooms are created in the Dojo.
        """
        my_dojo = Dojo()
        initial_room_count = len(my_dojo.living_space) + len(my_dojo.office)
        yellow_room = my_dojo.create_room('Kitchen', ['Yellow'])
        new_room_count =len(my_dojo.living_space) + len(my_dojo.office)
        self.assertEqual(new_room_count - initial_room_count,0 ,
                        msg ="Creation of Rooms other done Office and LivingSpace not possible")
