import unittest
from myapp.dojo.models.dojo import *
from myapp.dojo.models.person import *
from myapp.dojo.models.room import *

class TestAddPersonRoom(unittest.TestCase):

    def test_add_person_succesfully(self):
        my_dojo = Dojo()
        initial_person_count = 0
        add_elvis = my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        add_ezekiel = my_dojo.add_person('1002','Mugaya','Ezekiel','Fellow','N')
        self.assertEqual(my_dojo.add_person('1003','Kironde','Victor','Staff'),
                                       'Staff Kironde Victor has been successfully added.',
                                       msg ='Person Creation Not succesful.')
        self.assertEqual(my_dojo.add_person('1004','Kibuuka','Victor','Fellow'),
                                       'Staff Kibuuka Victor has been successfully added.',
                                       msg ='Person Creation Not succesful.')
        new_person_count = len(my_dojo.persons)
        self.assertEqual(new_person_count - initial_person_count, 4)

    def test_adding_existing_person(self):
        my_dojo = Dojo()
        add_elvis = my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
        add_ezekiel = my_dojo.add_person('1002','Mugaya','Ezekiel','Fellow','N')
        self.assertEqual(my_dojo.add_person('1001','Mulinde','Elvis', 'Staff'),
                                       'Person already exists',
                                       msg='Should not add existing person')
        self.assertEqual(my_dojo.add_person('1002','Mugaya','Ezekiel','Fellow','Y'),
                                       'Person already exists',
                                       msg='Should not add existing person')

    def test_adding_person_with_invalid_person_type(self):
        my_dojo = Dojo()
        self.assertEqual(my_dojo.add_person('1001','Mulinde','Elvis','Chef'),
                                       'Person is either \'Fellow\' or \'Student\'',
                                       msg ='Person type must be Fellow or Student')
        self.assertEqual(my_dojo.add_person('1002','Mugaya','Ezekiel','Musician','N'),
                                       'Person is either \'Fellow\' or \'Student\'',
                                       msg ='Person type must be Fellow or Student')

    def test_allocate_room_when_adding_person(self):
        my_dojo = Dojo()
        self.assertEqual(my_dojo.allocate_room('id','room_type'), 'Ezekiel has been allocated a Room',
                                          msg='Room Allocation Failed')

    def test_allocate_living_room_to_staff(self):
        my_dojo = Dojo()
        self.assertEqual(my_dojo.allocate_room('id','room_type'),
                                               'Staff are not allocated Living Space',
                                               msg ='Should not allocate Living Space to Staff')
