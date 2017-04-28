import unittest
from myapp.dojo.models.dojo import *
from myapp.dojo.models.person import *
from myapp.dojo.models.room import *

class TestReallocatePerson(unittest.TestCase):
    """
    This Test Class is used to make sure that functinality of reallocate_person works according to the specifications
    The type of the room you want the person to be assigned to used to make sure that reallocation is done only that very type.
    e.g. If a Fellow has an office blue, but no leaving space. You can not allocate him to a leaving space. For that you need to call allocate.
    Reallocation can not be used on staff that dont exist in the dojo.
    """
    def test_reallocate_succesful(self):
        """
        This test case is to ensure that the reallocation fuctionality works and it's only dono in the same room types.

        """
        my_dojo = Dojo()
        my_dojo.create_room('Office', ['Blue'])
        my_dojo.add_person('1001', 'Ezekiel', 'Mugaya', 'STAFF')
        ezekiel_current_room = my_dojo.persons['1001'].proom_name
        my_dojo.create_room('Office', ['Yellow'])
        my_dojo.reallocate_person('1001','Yellow')
        ezekiel_new_room = my_dojo.persons['1001'].proom_name
        self.assertEqual(ezekiel_new_room,'yellow', msg='Reallocation in the same room type succesful')

    def test_fail_reallocating_staff_to_living_space(self):
        """
        This test case is to ensure that staff are assigned to livingspace during reallocation
        """
        my_dojo = Dojo()
        my_dojo.create_room('Office', ['Blue'])
        my_dojo.add_person('1001', 'Ezekiel', 'Mugaya', 'STAFF')
        ezekiel_current_room = my_dojo.persons['1001'].proom_name
        my_dojo.create_room('living_space', ['Yellow'])
        my_dojo.reallocate_person('1001','Yellow')
        ezekiel_new_room = my_dojo.persons['1001'].proom_name
        self.assertEqual(ezekiel_new_room,'blue',
                        msg='Reallocation of staff to LivingSpace Unsuccesful')

    def test_leave_person_in_current_room_if_room_being_reallocated_to_is_full_or_not_already_created(self):
        """
        This test case is to ensure that reallocation leaves the person in that same room if unsuucesful
        """
        my_dojo = Dojo()
        my_dojo.create_room('Office', ['Blue'])
        my_dojo.add_person('1001', 'Ezekiel', 'Mugaya', 'STAFF')
        ezekiel_current_room = my_dojo.persons['1001'].proom_name
        my_dojo.reallocate_person('1001','Yellow')
        ezekiel_new_room = my_dojo.persons['1001'].proom_name
        self.assertEqual(ezekiel_new_room,'blue',
                        msg='Reallocation of staff to unavailble room or ful room is not possible. Leaves person in same room')
