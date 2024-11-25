"""
allow the user to use our command line library
purchase.py <product_name> <product_price> <product_type> <payment_given>

"""

import sys
import os

# create a class name product

class Product(object):
    def __init__(self, name, price, payment_type, given):
        self.name = name if len(name) >= 3 else "Default Name"
        # ensure price is a float and value is greater than 0
        self.price = price if isinstance(price, float) and price >= 0 else 0.05
        self.payment_type = payment_type if payment_type in "debit, credit, cash".split(",") else "cash"
        # price given must be great or equal to the amount
        self.given = given if isinstance(given, float) and given >= self.price else 0

    def write_to_file(self):
        path = os.path.join(os.path.dirname(__file__), self.name + ".txt")
        open(path, 'w').write(self.__str__())

    def change_to_give_back(self):
        return self.given - self.price
    # sumary mthod
    def __str__(self):
        return (f'Name={self.name},'
                f'Price= {self.price},'
                f'Payment Type- {self.payment_type},'
                f'Payment Given- {self.given}')



try:

    if len(sys.argv) != 5:
        print(f"Usage: {os.path.basename(__file__)} purchase.py <product_name> " 
              "<product_price> <product_type> <payment_given>")
        exit()
    product_name = sys.argv[1]
    product_price = float(sys.argv[2])
    payment_type = sys.argv[3]
    payment_given = float(sys.argv[4])
    product = Product(name=product_name,
                      price=product_price,
                      payment_type=payment_type,
                      given=payment_given)
    print(product)
    print("Change to give back = ", product.change_to_give_back())
except Exception as e:
    print(e, file=sys.stderr)




