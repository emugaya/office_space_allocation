import unittest


from myapp.dojo.models.dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    def test_create_room_succesfully(self):
        my_dojo = Dojo()
        initial_room_count = len(my_dojo.living_space) + len(my_dojo.office)
        blue_office = my_dojo.create_room('office', 'Blue')
        brown_living_space = my_dojo.create_room('LivingSpace', 'Brown')
        self.assertTrue(blue_office)
        self.assertTrue(brown_living_space)
        # self.assertIsInstance(blue_office, 'Office')
        self.assertEqual(my_dojo.create_room('Office','Mugaya'), 'An Office called Mugaya has been successfully created!',
                              msg='Room Creation not succesful')
        new_room_count =len(my_dojo.living_space) + len(my_dojo.office)
        self.assertEqual(new_room_count - initial_room_count,3 )

    def test_create_room_when_room_already_exists(self):
        my_dojo = Dojo()
        blue_office = my_dojo.create_room('office', 'blue')
        brown_living_space = my_dojo.create_room('LivingSpace', 'Brown')
        self.assertEqual(my_dojo.create_room('Office', 'Blue'),
                                        'Office already exists.',
                                        msg='Creating a Office with the same name isn not allowed')
        self.assertEqual(my_dojo.create_room('LivingSpace', 'Brown'),
                                         'Living Space already exists.',
                                         msg='Creating a Office with the same name isn not allowed')

    def test_create_invalid_room_type(self):
        my_dojo = Dojo()
        self.assertEqual(my_dojo.create_room('Kitchen', 'Yellow'),
                                        'Invalid Room Type',
                                        msg='Room type should be either an \'Office\' or \'LivingSpace\'')

    def test_create_room_name_data_types_being_passed(self):
        my_dojo = Dojo()
        self.assertEqual(my_dojo.create_room('Office', {'name':'office'}),
                                         'Room Name Entries must be strings.',
                                         msg ='Variables being passed to create_room are not strings')

    def test_create_room_with_empty_name_arguements(self):
        my_dojo = Dojo()

        self.assertEqual(my_dojo.create_room('LivingSpace', ' '),
                                        'You didn\'t provide room name, please try again',
                                        msg = 'Room name and type must be entered')
        self.assertEqual(my_dojo.create_room('Office', ' '),
                                        'You didn\'t provide room name, please try again',
                                        msg = 'Room name and type must be entered')


if __name__ == '__main__':
    unittest.main()
