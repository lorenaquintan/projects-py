"""
Python OOP Assignment Part 2: Vehicle & Truck

Objective: To understand the advanced concepts of classes, inheritance & polymorphism

"""

# Task 1
class Vehicle:
    color_options = ['pink', 'red', 'blue', 'yellow', 'light green']
    doors_options = [2, 4, 5]
    # 3. Create a constructor that takes 3 arguments and passes each argument to the appropriate property.

    def __init__(self, color, number_of_doors, gas_powered):
        # The class will have the following PRIVATE attributes
        self.color = color
        self.number_of_doors = number_of_doors
        self.gas_powered = gas_powered

    # 2. Each private attribute will have restricted values
    # 4. Create the getters and setters for the private attributes

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if isinstance(value, str) and value.lower() in Vehicle.color_options:
            self.__color = value
        elif isinstance(value, (int, float, bool)):
            raise TypeError(f"Must be a string value!")
        else:
            raise ValueError(f"The only available color options are: {Vehicle.color_options}")

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        if isinstance(value, int) and value in Vehicle.doors_options:
            self.__number_of_doors = value
        elif isinstance(value, (str, float, bool)):
            raise TypeError(f"Must be an whole number value!")
        else:
            raise ValueError(f"Only these number of doors allowed: {Vehicle.doors_options}")

    @property
    def gas_powered(self):
        return self.__gas_powered

    @gas_powered.setter
    def gas_powered(self, value):
        if isinstance(value, bool):
            self.__gas_powered = value
        else:
            raise TypeError('Invalid value! Must be a boolean value')

    # 5. Override the toString method to summarize all instance variables of the class
    def __str__(self):
        return (f"Color of the Vehicle: {self.__color}\n"
                f"Number of Doors: {self.__number_of_doors}\n"
                f"Is the vehicle Gas powered: {self.__gas_powered}")

    # 6. Create a method named is_eco_friendly()
    def is_eco_friendly(self):
        if self.number_of_doors == 2 and not self.gas_powered:
            return True
        else:
            return False

# Task 2
# 1. Create a class named Truck that is based on the Vehicle class
class Truck(Vehicle):
    # 1.3. Create a constructor that takes 5 arguments and passes each argument to the appropriate property.
    def __init__(self, color, number_of_doors, gas_powered, NSeats, trunk_space):
        super().__init__(color, number_of_doors, gas_powered)

        # Create two additional private attributes
        self.NSeats = NSeats
        self.trunk_space = trunk_space

    @property
    def NSeats(self):
        return self.__NSeats

    @NSeats.setter
    # 1.2. corresponds to the data type outlined about and has a value greater than zero
    def NSeats(self, value):
        if isinstance(value, int) and value > 0:
            self.__NSeats = value
        elif isinstance(value, (float, str, bool)):
            raise TypeError(f"Invalid! Must be a whole number value!")
        else:
            raise ValueError(f"Invalid! Number should be above 0!")

    @property
    def trunk_space(self):
        return self.__trunk_space

    @trunk_space.setter
    def trunk_space(self, value):
        if isinstance(value, int) and value > 0:
            self.__trunk_space = value
        elif isinstance(value, (float, str, bool)):
            raise TypeError(f"Invalid! Must be a whole number value!")
        else:
            raise ValueError(f"Invalid! Number Should be above 0!")

    # 1.4. Override the toString method to summarize all properties variables of the class
    def __str__(self):
        return (super().__str__() +
                (f"\nNumber of Seats: {self.__NSeats}\n"
                f"Trunk space allocated: {self.__trunk_space}"))

    # 2. Override the is_eco_friendly() method.
    # it also determines if the Truck has at most two seats and has no trunk space.
    def is_eco_friendly(self):
        old_eco_friendly = super().is_eco_friendly()
        add_eco_friendly = self.__NSeats <= 2 and self.__trunk_space == 0
        return old_eco_friendly + add_eco_friendly

# Vehicles
#Barbie_V = Truck("pink", 2, True, 2, 2)
#Bob_Dylan_V = Truck("black", 5, False, 5, 6)
# Calling
#print(Barbie_V)
#print(Barbie_V.is_eco_friendly())
#print(Bob_Dylan_car)