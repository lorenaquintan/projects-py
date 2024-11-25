# Task 6
from task5 import Apartment

# Create an Apartment object and pass 5 arguments
apartment_1 = Apartment(2, 1, "automatic", "carpet",1084)
# Output the two new properties of Apartment class
print(f"The Apartment has {apartment_1.floor_type} floors.")
print(f"The Apartment is {apartment_1.square_ft} Sq.ft.")

# Change the values of the two new properties of Apartment by using the setters.
apartment_1.floor_type = "green tiles"
apartment_1.square_ft = 1000

# Output the toString of Apartment to display all five properties
print(apartment_1.__str__())