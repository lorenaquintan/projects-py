# Task 3

# Create a class called Home
class Home:
    # Create a constructor that takes 3 arguments
    # and passes each argument to the appropriate property
    def __init__(self, num_of_rooms, num_of_doors, door_type):
        # three properties that cannot be accessible outside of the class.
        self.__num_of_rooms = num_of_rooms
        self.__num_of_doors = num_of_doors
        self.__door_type = door_type

    # Create the accessors and mutators for these properties.
    @property
    # getter
    def num_of_rooms(self):
        return self.__num_of_rooms
    @num_of_rooms.setter
    # setter
    def num_of_rooms(self, value):
        self.__num_of_rooms = value

    @property
    def num_of_doors(self):
        return self.__num_of_doors
    @num_of_doors.setter
    def num_of_doors(self, value):
        self.__num_of_doors = value

    @property
    def door_type(self):
        return self.__door_type
    @door_type.setter
    def door_type(self, value):
        self.__door_type = value