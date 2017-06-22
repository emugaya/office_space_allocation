import unittest
from dojo.models.dojo import Dojo

class TestLoadPeople(unittest.TestCase):
    """
    This Object Tests Fuctionality of the load_people method in the dojo
    """
    def test_load_people_succesful(self):
        """
        This test case is to check whether users are succesfully loaded if data
        provided in the input file is in the right format
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        #Check that dojo has no people
        self.assertEqual(len(my_dojo.persons),
                                0, msg='new object contains persons')
        #Check that office room blue has no people
        self.assertEqual(len(my_dojo.office['blue'].members),
                                0, msg='new object contains persons')
        #Check that livingspace blue has no people
        self.assertEqual(len(my_dojo.living_space['pink'].members),
                                0, msg='new object contains persons')
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        #Check that dojo has 6 people
        self.assertEqual(len(my_dojo.persons),
                                6, msg='new object contains persons')
        #Check that office room blue has 6 people
        self.assertEqual(len(my_dojo.office['blue'].members),
                                6, msg='new object contains persons')
        #Check that livingspace blue has 6 people
        self.assertEqual(len(my_dojo.living_space['pink'].members),
                                2, msg='new object contains persons')


    def test_load_people_notifies_users_if_filename_provided_is_not_txt(self):
        """
        This tests whether a user gets a notification that the file provided is incorrect
        when they supply a file that doesn't exist or not txt.
        """
        pass

    def test_load_people_generates_file_with_errors_in_upload_file(self):
        """
        This tests whether load_people generates a file that has lines with errors for a user
        during the load_people function and informs them that there were errors.
        """
        pass
