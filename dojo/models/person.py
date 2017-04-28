class Person(object):
    def __init__(self, person_id, last_name, first_name):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name =first_name

class Fellow(Person):
    def __init__(self, person_id, last_name, first_name,person_type="Fellow", wants_accommodation ='', proom_name='', lroom_name =''):
        super(Fellow, self).__init__(person_id, last_name, first_name)
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation
        self.proom_name = proom_name
        self.lroom_name = lroom_name


class Staff(Person):
    def __init__(self,person_id, last_name, first_name, person_type='STAFF', proom_name=''):
        super(Staff, self).__init__(person_id, last_name, first_name)
        self.person_type = person_type
        self.proom_name = proom_name
