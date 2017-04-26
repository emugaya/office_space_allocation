class Person(object):
    def __init__(self, person_id, last_name, first_name):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name =first_name
        self.room_name = ''

class Fellow(Person):
    def __init__(self, person_id, last_name, first_name,person_type, wants_accommodation =None, proom_name=''):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation
        self.proom_name = proom_name


class Staff(Person):
    def __init__(self,person_id, last_name, first_name, person_type, proom_name=''):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.person_type = person_type
        self.room_name =''
