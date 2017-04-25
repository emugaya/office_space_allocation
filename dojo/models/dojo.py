from myapp.dojo.models.person import Person, Staff, Fellow
from myapp.dojo.models.room import Office, LivingSpace

class Dojo(object):
    def __init__(self):
        self.fellow = []
        self.staff = []
        self.living_space = {}
        self.office = {}
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



my_dojo = Dojo()
l = my_dojo.create_room('office', 'Black')
print(l)

print(my_dojo.office)
