import unittest
from dojo.models.dojo import Dojo

class TestAllocateRoom(unittest.TestCase):
    """
    This Class Tests the allocate_room method in the dojo.
    """
    def test_allocate_staff_office_room_succesfully(self):
        """
        This Class tests whether allocating staff offic room is succesful.
        It calls create_room to have the room created and then,
        call methods add_person which automatically calls allocate_room method
        """
        my_dojo = Dojo()
        initial_count_staff_with_office_list = len(my_dojo.staff_with_office_list)
        my_dojo.create_room('office', ['Blue'])
        my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        new_count_staff_with_office_list = len(my_dojo.staff_with_office_list)
        self.assertEqual((new_count_staff_with_office_list - initial_count_staff_with_office_list), 1,
                            msg="Staff Allocation succesful")

    def test_allocate_staff_office_room_unsuccesfully(self):
        """
        This Class tests whether allocating staff room is succesful:
        I calls methods add_person which automatically calls allocate_room method
        """
        my_dojo = Dojo()
        initial_count_staff_with_office_list = len(my_dojo.staff_with_office_list)
        my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        new_count_staff_with_office_list = len(my_dojo.staff_with_office_list)
        self.assertEqual((new_count_staff_with_office_list - initial_count_staff_with_office_list), 0,
                            msg="Staff Office Allocation Unsuccesful Works")

    def test_allocate_fellow_office_succesful(self):
        """
        This Class tests whether allocating staff room is succesful:
        It calls create_room to create rooms before making the check.
        It calls methods add_person which automatically calls allocate_room method
        """
        my_dojo = Dojo()
        initial_fellows_with_office_list = len(my_dojo.fellows_with_office_list)
        my_dojo.create_room('office', ['Blue'])
        my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        new_count_fellows_with_office_list = len(my_dojo.fellows_with_office_list)
        self.assertEqual((new_count_fellows_with_office_list - initial_fellows_with_office_list), 0,
                            msg="Fellow Office Allocation Succesful Works")

    def test_allocate_fellow_office_unsuccesful(self):
        """
        This Class tests whether allocating a fellow living space was unsuucesful due to not having office rooms
        It calls methods add_person which automatically calls allocate_room method
        """
        my_dojo = Dojo()
        initial_fellows_who_missed_living_space = len(my_dojo.fellows_who_missed_living_space)
        my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        new_count_fellows_who_missed_living_space = len(my_dojo.fellows_who_missed_living_space)
        self.assertEqual((new_count_fellows_who_missed_living_space - initial_fellows_who_missed_living_space), 0,
                            msg="Fellow Office Allocation Unsuccesful Works")

    def test_allocate_fellow_living_room_succesful(self):
        """
        This Class tests whether a fellow is succesfully allocated a living space if they want it
        I calls methods add_person which automatically calls allocate_room method
        """
        my_dojo = Dojo()
        initial_count_fellows_with_living_room_list = len(my_dojo.fellows_with_living_room_list)
        my_dojo.create_room('livingspace', ['Blue'])
        my_dojo.add_person('1001','Mulinde','Elvis', 'Fellow','Y')
        new_count_fellows_with_living_room_list = len(my_dojo.fellows_with_living_room_list)
        self.assertEqual((new_count_fellows_with_living_room_list - initial_count_fellows_with_living_room_list), 1,
                            msg="Fellow allocation of LivingSpace Succesful")

    def test_allocate_staff_living_space_unsuccesful(self):
        """
        This Class tests whether allocating staff living space unsuccesful since staff are not supposed to have living spaces
        I calls methods add_person which automatically calls allocate_room method
        """
        my_dojo = Dojo()
        my_dojo.create_room('LivingSpace', ['Blue'])
        initial_number_of_members_in_living_space = len(my_dojo.living_space['blue'].members)
        my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        new_number_of_members_in_living_space = len(my_dojo.living_space['blue'].members)
        self.assertEqual((new_number_of_members_in_living_space - initial_number_of_members_in_living_space), 0,
                            msg="Staff Allocation of Living Space Unsuccesful Works")

    def test_not_allocating_fellow_who_dont_want_living_space_succesful(self):
        """
        This Class tests whether not allocating living spaces to fellows who don't want living space was room is succesful:
        I calls methods add_person which automatically calls allocate_room method
        """
        my_dojo = Dojo()
        my_dojo.create_room('LivingSpace', ['Blue'])
        initial_number_of_members_in_living_space = len(my_dojo.living_space['blue'].members)
        my_dojo.add_person('1001','Mulinde','Elvis', 'Fellow')
        new_number_of_members_in_living_space = len(my_dojo.living_space['blue'].members)
        self.assertEqual((new_number_of_members_in_living_space - initial_number_of_members_in_living_space), 0,
                            msg="Staff Allocation of Living Space Unsuccesful Works")
