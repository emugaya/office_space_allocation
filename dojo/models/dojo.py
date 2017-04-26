# from myapp.dojo.models.person import Person, Staff, Fellow
from dojo.models.person import Person, Staff, Fellow
from dojo.models.room import Office, LivingSpace
import random

class Dojo(object):
    """
    Dojo is an Object that is used to maanage Room Allocation in the Dojo.
    It has funtions create_room, add_person
    """
    def __init__(self):
        self.fellow = []
        self.staff = []
        self.living_space = {}
        self.office = {}
        self.persons ={}
        self.room_types = ['office','livingspace'] #Initialize Room types
        self.person_types =['STAFF', 'FELLOW'] # Initialize person types
    def create_room(self, room_type, *room_name):
        rooms_list = list(room_name)[0]
        for room in rooms_list:
            if room_type.lower() in self.room_types:
                room_name_1 = room
                room = room.lower().strip()
                if room_type.lower() == 'office':
                    if room in self.office:
                        print('Office already exists')
                        return 'Office already exists.'
                    else:
                        new_room = Office(room)
                        self.office[room] = Office(room)
                        print('An Office called ' + room_name_1 + ' has been successfully created!')

                if room_type.lower() == 'livingspace':
                    if room in self.living_space:
                        print(room.upper()+ ' Living Space already Exists')
                    else:
                        new_room = LivingSpace(room)
                        self.living_space[room] = LivingSpace(room)
                        print('A LivingSpace called ' + room_name_1 + ' has been successfully created!')
            else:
                print("Invalid Room Type")
                #return "Invalid Room Type"

    def add_person(self, person_id, last_name, first_name, person_type, wants_accommodation = None):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation
        self.person_type = self.person_type.strip().upper()
        if self.person_type in self.person_types:
            if self.person_id in self.persons:
                print('Person already exists')
                return 'Person already exists'
            elif person_type.upper() == 'FELLOW':
                self.persons[self.person_id] = Fellow(self.person_id, self.last_name, self.first_name, self.person_type, self.wants_accommodation)
                print('Fellow '+ last_name + ' ' + first_name + ' has been successfully added.')
                offices_list = []
                for key in self.office.keys():
                    if len(self.office[key].members) < 6:
                        offices_list.append(key)
                if not offices_list:
                    print('There are no offices available for allocation, create some')
                    return 'There are no offices available for allocation, create some'
                office = random.choice(offices_list)
                self.office[office].members.append(person_id)
                print(self.persons[person_id].first_name + ' has been allocated office ' + office)
                #Check if Fellow Wants Accomodation
                if wants_accommodation == 'Y':
                    living_space_list = []
                    for key in self.living_space.keys():
                        if len(self.living_space[key].members) < 4:
                            living_space_list.append(key)
                    if not living_space_list:
                        print ('There are no livingspaces available, Create some')
                        return 'There are no livingspaces available, Create some'
                    living_space_room = random.choice(living_space_list)
                    self.living_space[living_space_room].members.append(person_id)
                    print(self.persons[person_id].first_name + ' has been allocated Living Space ' + living_space_room)
            #Allocate Room to staff
            else:
                self.persons[self.person_id] = Staff(self.person_id, self.last_name, self.first_name, self.person_type)
                print('Staff '+ last_name + ' ' + first_name + ' has been successfully added.')
                offices_list = []
                for key in self.office.keys():
                    if len(self.office[key].members) < 6:
                        offices_list.append(key)
                if not offices_list:
                    print('There are no offices available for allocation, create some')
                    return 'There are no offices available for allocation, create some'
                office = random.choice(offices_list)
                self.office[office].members.append(person_id)
                print(self.persons[person_id].first_name + ' has been allocated office ' + office)
                return self.persons[person_id].first_name + ' has been allocated office ' + office

        else:
            print('Person is either \'Fellow\' or \'Student\'')
            return 'Person is either \'Fellow\' or \'Student\''

    def print_room(self,room_name):
        """
        This method prints names of members in a room supplied
        """
        self.room_name = room_name

        if not isinstance(room_name,str):
            print ("Room name must be a string")
        if room_name.lower() in self.office:
            if len(self.office[room_name].members) == 0:
                print(room_name.upper() + ' has no members')
            else:
                print ('Office Room '+ room_name.upper())
                print('-----------------------------------------------------------------')
                for name in self.office[room_name].members:
                    s = self.persons[name].last_name + ' ' +self.persons[name].first_name +','
                    print(s, end =" "  )
                print()
        elif room_name.lower() in self.living_space:
            if len(self.living_space[room_name].members) == 0:
                print('Office ' + room_name.upper() + ' has no members')
            else:
                print ('Living Space Room '+room_name.upper())
                print('-----------------------------------------------------------------')
                for name in self.living_space[room_name].members:
                    s = self.persons[name].last_name + ' ' +self.persons[name].first_name + ','
                    print(s ,end=" ")
                print()
        else:
            print('Your room doesn\'t exist')

    def print_allocations(self, filename=""):
        if not filename:
            print('Living Space Allocations')
            print('-----------------------------------------------------------------')
            print()
            for room in self.living_space:
                self.print_room(room)
            print('Office Space Allocations')
            for room in self.office:
                self.print_room(room)
        else:
            my_file = open(filename + ".txt", "w")
            #my_file.write('Living Space Allocations\n')
            my_file.write('\n')
            my_file.write('-----------------------------------------------------------------\n')
            #my_file()
            for room_name in self.office:
                if room_name.lower() in self.office:
                    if len(self.office[room_name].members) == 0:
                        my_file.write(room_name.upper() + ' has no members')
                    else:
                        my_file.write ('Office Room '+ room_name.upper() +'\n')
                        my_file.write('-----------------------------------------------------------------\n')
                        for name in self.office[room_name].members:
                            my_file.write(self.persons[name].last_name + ' ' +self.persons[name].first_name +', ')
                        my_file.write('\n')
                elif room_name.lower() in self.living_space:
                    if len(self.living_space[room_name].members) == 0:
                        my_file.write('Office ' + room_name.upper() + ' has no members')
                    else:
                        my_file.write ('Living Space Room '+room_name.upper())
                        my_file.write('-----------------------------------------------------------------')
                        for name in self.living_space[room_name].members:
                            s = self.persons[name].last_name + ' ' +self.persons[name].first_name + ','
                            my_file.write(s ,end=" ")
                        my_file.write('\n')
                my_file.close()
