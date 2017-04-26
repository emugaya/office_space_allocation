class Person(object):
    def __init__(self, id, last_name, first_name):
        self.last_name = last_name
        self.first_name =first_name

class Fellow(Person):
    def __init__(self, person_id, last_name, first_name,person_type, wants_accommodation =None):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation

class Staff(Person):
    def __init__(self,person_id, last_name, first_name,person_type):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.person_type = person_type
