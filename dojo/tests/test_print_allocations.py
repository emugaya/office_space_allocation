import os
import unittest
from dojo.models.dojo import Dojo

class TestPrintAllocations(unittest.TestCase):
    """
    This Object Tests Fuctionality of the print_alllocations
    """
    def test_print_allocations_succesfully(self):
        """
        This case tests whether print_allocations succesfully returns rooms
        and there members to be printed on the screen or file.
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        self.assertEqual(my_dojo.print_allocations,
                               {'blue': ['Mugaya Ezekiel',
                                          'Roza Kobel',
                                          'Favour Kwagala',
                                          'Joyce Mummy',
                                          'Isiaha Katumwa',
                                          'Paul Kobel'],\
                                'pink': ['Roza Kobel','Paul Kobel']
                                },
                                msg = "Print Allocations doesn't return values to be printed to screen"
                                )

    def test_print_allocations_prints_to_file(self):
        """
        This case tests whether print_allocations prints to a file if the file name is supplied.
        """
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')

        self.assertEqual(my_dojo.print_allocations('test_print_allocations_file'),
                                                   "Allocations Have been \
                                                   printed to file succesfully",
                                                   msg="Allocations not succesfully printed to file"
                                                   )
        self.assertEqual(os.path.exists('test_print_allocations_file.txt'),True , msg="File not created")
