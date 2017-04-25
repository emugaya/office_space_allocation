class Person(object):
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name =first_name

class Fellow(Person):
    def __init__(self, last_name, first_name, wants_accommodation ='N'):
        self.last_name = last_name
        self.first_name = first_name
        self.wants_accommodation = wants_accommodation

class Staff(Person):
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
