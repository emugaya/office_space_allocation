class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name
        self.members = []

class Office(Room):
    def __init__(self, room_name):
        self.room_name = room_name
        self.members = []

class LivingSpace(Room):
    def __init__(self, room_name):
        self.room_name = room_name
        self.members = []
