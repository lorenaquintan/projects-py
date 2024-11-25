# Task 5
from task3 import Home

# Create a class called Apartment that is based on the Home class.
class Apartment(Home):
    def __init__(self, num_of_rooms, num_of_doors, door_type, floor_type, square_ft):
        # 3 Home properties
        super().__init__(num_of_rooms, num_of_doors, door_type)

        # 2 new prop of apt
        self.__floor_type = floor_type
        self.__square_ft = square_ft

    @property
    def floor_type(self):
        return self.__floor_type

    @floor_type.setter
    def floor_type(self, value):
        self.__floor_type = value

    @property
    def square_ft(self):
        return self.__square_ft

    @square_ft.setter
    def square_ft(self, value):
        self.__square_ft = value

    # Override the toString to include the summary of the two
    # new properties of Apartment AND the three properties of Home
    def __str__(self):
        return (f"\n~Apartment information~ \n"
                f"Number of rooms: {self.num_of_rooms}\n"
                f"Number of doors: {self.num_of_doors}\n"
                f"Door Material: {self.door_type}\n"
                f"Floor Material: {self.__floor_type}\n"
                f"Square ft of apartment: {self.__square_ft} sq.ft.")
