import unittest
from dojo.models.dojo import Dojo

class TestSaveAndLoadState(unittest.TestCase):
    """ This test case is used to test persistence of data to the database.
    It tests fucntionality of save_state and load_methods in dojo\models\dojo.py
    """
    def test_save_and_load_state(self):
        #create new Dojo Object.
        my_dojo = Dojo()
        #create rooms in the dojo
        my_dojo.create_room('office', [
                                        'Blue',
                                        'Red',
                                        'Purple',
                                        'Green',
                                        'Andela',
                                        'Uganda',
                                        'Tanzania'
                                        ])
        my_dojo.create_room('livingspace', ['Pink', 'Orange', 'Kenya', 'Greyish'])
        # Add people to dojo from text file
        my_dojo.load_people('read_data')
        number_of_persons_in_my_dojo = len(my_dojo.persons)
        number_of_offices_in_my_dojo  = len(my_dojo.office)
        number_of_living_space_in_my_dojo  = len(my_dojo.living_space)
        my_dojo.save_state('test_dojo_save_state')
        # Create new Dojo Object
        my_dojo_1 = Dojo()
        # Test that offices and living space are empty
        self.assertEqual(len(my_dojo_1.persons),
                                0, msg='new object contains persons')
        self.assertEqual(len(my_dojo_1.office),
                                0, msg='new object contains offices')
        self.assertEqual(len(my_dojo_1.living_space),
                                0, msg='new object contains living spaces')
        # Load saved state test_dojo_save_state in this new object
        my_dojo_1.load_state('test_dojo_save_state')
        #Test that it has the same values as the first object after loadind state
        self.assertEqual(len(my_dojo_1.persons),
                              number_of_persons_in_my_dojo,
                              msg='Values not Equal, Save and Load state failed')
        print('Save state')
        self.assertEqual(len(my_dojo_1.office),
                              number_of_offices_in_my_dojo,
                              msg='Values not Equal, Save and Load state failed')
        self.assertEqual(len(my_dojo_1.living_space),
                              number_of_living_space_in_my_dojo,
                              msg='Values not Equal, Save and Load state failed')
