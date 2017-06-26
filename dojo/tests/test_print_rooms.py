import unittest
from dojo.models.dojo import Dojo

class TestPrintRoom(unittest.TestCase):
    """
    This Object Tests Fuctionality of the print_room method in the dojo
    """
    def test_print_room_succesfully(self):
        """
        This test case is used to check that print_room method prints the wright items on the screen
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        #Test that printing and existing room with members is sucessful.
        self.assertEqual(my_dojo.print_room('pink'),{'pink' :['Roza Kobel',
                                                             'Paul Kobel']},
                                                    msg='Print room unsuccesful')
        self.assertEqual(my_dojo.print_room('blue'),{'blue':['Mugaya Ezekiel',
                                                           'Roza Kobel',
                                                           'Favour Kwagala',
                                                           'Joyce Mummy',
                                                           'Isiaha Katumwa',
                                                           'Paul Kobel']},
                                                 msg="Print Room unsuccesful")

    def test_printing_unexisting_room_unsuccessful(self):
        """
        This tests whether a user receives a notification that the room they want to
        print members for does not exist
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        #Test that user gets an error msg that wrong roomnamewas supplied
        self.assertEqual(my_dojo.print_room('yellow'), "Your room doesn't exist",
                                                      msg = "User not notified when wrong room name is supplied name")
        self.assertEqual(my_dojo.print_room('green'), "Your room doesn't exist",
                                                      msg = "User not notified when wrong room name is supplied name")

    def test_print_empty_room(self):
        """
        This tests whether users get notified that the room they have requested to print has no members assigned to it.
        """
        #create new Dojo Object.
        my_dojo = Dojo()
        #create an office room in the dojo
        my_dojo.create_room('office', ['Blue'])
        #create a living room in the dojo
        my_dojo.create_room('livingspace', ['Pink'])
        # Add 6 people(4 staff and 2 fellows) to dojo from text file by calling load_people
        my_dojo.load_people('load_people_data')
        #Test that user gets an error msg that wrong roomnamewas supplied
        my_dojo.create_room('livingspace', ['Green'])

        self.assertEqual(my_dojo.print_room('green'),"Room has no members no members",
                                                    msg="User not notified that room has no members")
