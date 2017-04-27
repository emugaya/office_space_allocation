class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name
        self.members =[]


class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.max_num = 6


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
        self.max_num = 4
