import unittest
from dojo.models.dojo import Dojo

class TestPrintUnallocated(unittest.TestCase):
    """
    This Object Tests Fuctionality of the print_room method in the dojo
    """
    def test_printing_unallocated_to_screen_succesfully(self):
        """
        This tests whether, print_unallocated succesfully prints to the screen
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        my_dojo.load_people('load_people_data2')
        self.assertEqual(my_dojo.print_unallocated,
                         {'staff_who_missed_office_list':[],
                           'fellows_who_missed_office':[],
                           'fellows_who_missed_living_space':[]},
                            msg="Incorrect Unallocationsns")


    def test_print_unllocated_writes_to_file_succesfully(self):
        """
        This case tests whether print_unllocated succesfully writes to file if
        filename is provided
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        # Add 7 people with no rooms created to accomodate them
        my_dojo.load_people('load_people_data2')
        #Call Print unallocated to print to file.
        my_dojo.print_allocations('test_print_unllocated_file')
        #Test whether print unallocated printed to file.
        self.assertEqual(os.path.exists('test_print_unllocated_file.txt'),True , msg="File not created")


    def test_print_unallocated_persons_are_correct(self):
        """
        This test case tests whether print_unllocated values are correct
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        # Add 7 people with no rooms created to accomodate them
        my_dojo.load_people('load_people_data2')
        #Test whether the list of staff without office space is correct
        self.assertEqual(my_dojo.staff_who_missed_office_list,
                                        ['1012 WALTERS DOMINIC',
                                        '1015 RILEY LEIGH',
                                        '1017 McGUIRE KELLY'],
                                        msg='Incorrect list of staff who missed office')
        #Test whether the list of fellows without office space is correct
        self.assertEqual(my_dojo.fellows_who_missed_office,
                                        ['1011 SULE OLUWAFEMI',
                                        '1013 PATTERSON SIMON',
                                        '1014 LAWRENCE MARI',
                                        '1016 LOPEZ TANA'],
                                        msg='Incorrect list of staff who missed office')
        #Test whether the list of fellows who missed Living Space is correct
        self.assertEqual(my_dojo.fellows_who_missed_living_space,
                                        ['1014 LAWRENCE MARI', '1016 LOPEZ TANA'],
                                        msg='Incorrect list of staff who missed office')
