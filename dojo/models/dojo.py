from myapp.dojo.models.person import Person, Staff, Fellow
from myapp.dojo.models.room import Office, LivingSpace
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
            return 'Room Name Entries must be strings.'
        if len(room_name.strip()) ==0:
            return 'You didn\'t provide room name, please try again'
        if self.room_type.lower() in self.room_types:
            room_name_1 = self.room_name
            self.room_name = self.room_name.lower().strip()
            if self.room_type.lower() == 'office':
                if self.room_name in self.office:
                    return 'Office already exists.'
                else:
                    new_room = Office(room_name)
                    self.office[self.room_name] = Office(room_name)
                    print(self.office)
                    return 'An Office called ' + room_name_1 + ' has been successfully created!'
            if self.room_type.lower() == 'livingspace':
                if self.room_name in self.office:
                     return 'Living Space already exists.'
                else:
                    new_room = LivingSpace(room_name)
                    self.office[self.room_name] = Office(room_name)
                    print(self.office)
                    return 'A LivingSpace called ' + room_name_1 + ' has been successfully created!'

        else:
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
                return 'Person already exists'
            elif person_type == 'FELLOW':
                self.persons[self.person_id] = Fellow(self.person_id, self.last_name, self.first_name, self.person_type, self.wants_accommodation)
                print(self.persons)
                return ('Fellow '+ last_name + ' ' + first_name + ' has been successfully added.')
            else: #person_type == 'STAFF':
                self.persons[self.person_id] = Staff(self.person_id, self.last_name, self.first_name, self.person_type)
                print(self.persons)
                return ('Staff '+ last_name + ' ' + first_name + ' has been successfully added.')
        else:
            return 'Person is either \'Fellow\' or \'Student\''

    def allocate_room(self, person_id):






my_dojo = Dojo()
l = my_dojo.create_room('office', 'Black')
add_elvis = my_dojo.add_person('1001','Mulinde','Elvis', 'Staff')
add_ezekiel = my_dojo.add_person('1002','Mugaya','Ezekiel','Fellow','N')
print (add_ezekiel)
print (add_elvis)
print(l)

print(my_dojo.office)
print(my_dojo.persons)
