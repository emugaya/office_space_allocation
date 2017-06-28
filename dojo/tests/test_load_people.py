import unittest
import os
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
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        self.assertEqual(my_dojo.load_people('qwerty'),
                        "File Provided is neither .txt nor does it exist",
                        msg="Loading wrong file type or non existing file doesnt give an error")

    def test_load_people_generates_file_with_errors_in_upload_file(self):
        """
        This tests whether load_people generates a file that has lines with errors for a user
        during the load_people function and informs them that there were errors.
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        #Check whether filealready exists and delete it.
        try:
            os.remove('errors.txt')
        except OSError:
                pass
        # Load people with one line with errors
        my_dojo.load_people('load_people_data_errors')
        # Test whether load_people generates errors.txt
        self.assertEqual(os.path.exists('errors.txt'),True , msg="File not created")
        file_line = ''
        with open('errors.txt') as f:
            file_line = f.readline().strip()
        self.assertEqual(file_line,"101 Uganda line number (7)",msg="Errors file has incorrect information")
        #Delete errors.txt file after test
        try:
            os.remove('errors.txt')
        except OSError:
                pass

    def test_load_people_notifies_users_if_file_has_been_read_and_where_errors_are_saved(self):
        """
        This tests whether a user gets a notification when a file has been read
        succesfully and where errors have been saved errors.txt
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        self.assertEqual(my_dojo.load_people('load_people_data_errors'),
                    "File read succesfully, lines with errors have been written to 'errors.txt'",
                    msg="Loading wrong file type or non existing file doesnt give an error")
