# from myapp.dojo.models.person import Person, Staff, Fellow
from dojo.models.person import Person, Staff, Fellow
from dojo.models.room import Office, LivingSpace
import random

class Dojo(object):
    def __init__(self):
        self.fellow = []
        self.staff = []
        self.living_space = {}
        self.office = {}
        self.persons ={}
    def create_room(self, room_type, room_name):
        self.room_type = room_type
        self.room_name = room_name
        self.room_types = ['office','livingspace']
        if not isinstance(room_name,str):
            print('Room Name Entries must be strings.')
            return 'Room Name Entries must be strings.'
        if len(room_name.strip()) ==0:
            print('You didn\'t provide room name, please try again')
            return 'You didn\'t provide room name, please try again'
        if self.room_type.lower() in self.room_types:
            room_name_1 = self.room_name
            self.room_name = self.room_name.lower().strip()
            if self.room_type.lower() == 'office':
                if self.room_name in self.office:
                    print('Office already exists')
                    return 'Office already exists.'
                else:
                    new_room = Office(room_name)
                    self.office[self.room_name] = Office(room_name)
                    print('An Office called ' + room_name_1 + ' has been successfully created!')
                    return 'An Office called ' + room_name_1 + ' has been successfully created!'
            if self.room_type.lower() == 'livingspace':
                if self.room_name in self.office:
                    print(room_name.upper()+ ' Living Space already Exists')
                    return 'Living Space already exists.'
                else:
                    new_room = LivingSpace(room_name)
                    self.living_space[self.room_name] = LivingSpace(room_name)
                    print('A LivingSpace called ' + room_name_1 + ' has been successfully created!')
                    return 'A LivingSpace called ' + room_name_1 + ' has been successfully created!'

        else:
            print("Invalid Room Type")
            return "Invalid Room Type"

    def add_person(self, person_id, last_name, first_name, person_type, wants_accommodation = None):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation
        self.person_types =['STAFF', 'FELLOW']
        # if not len(self.person_id) and not len(self.last_name) and self.first_name and self.person_type:
        #     return 'All Fields must be properly filled'
        self.person_type = self.person_type.strip().upper()
        if self.person_type in self.person_types:
            if self.person_id in self.persons:
                print('Person already exists')
                return 'Person already exists'
            elif person_type.upper() == 'FELLOW':
                self.persons[self.person_id] = Fellow(self.person_id, self.last_name, self.first_name, self.person_type, self.wants_accommodation)
                print('Fellow '+ last_name + ' ' + first_name + ' has been successfully added.')
                #return ('Fellow '+ last_name + ' ' + first_name + ' has been successfully added.')
                # print(self.persons)
                #Allocate Fellow Office and optional Living Space
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
                #break
                #return self.persons[person_id].first_name + ' has been allocated office ' + office
                if wants_accommodation == 'Y':
                    living_space_list = []
                    for key in self.living_space.keys():
                        if len(self.living_space[key].members) < 4:
                            living_space_list.append(key)
                    if not living_space_list:
                        print ('There are no livingspaces available, Create some')
                        return 'There are no livingspaces available, Create some'
                    living_space_room = random.choice(living_space_list)
                    self.livingspace[living_space_room].append(person_id)
                    print(persons[person_id].first_name + ' has been allocated office ' + living_space_room)
                    #break
                    #return persons[person_id].first_name + ' has been allocated office ' + living_space_room

            else: #person_type == 'STAFF':
                self.persons[self.person_id] = Staff(self.person_id, self.last_name, self.first_name, self.person_type)
                print('Staff '+ last_name + ' ' + first_name + ' has been successfully added.')
                #break
                #return('Staff '+ last_name + ' ' + first_name + ' has been successfully added.')
                #print(self.persons)
                #Allocate Staff office
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

    
