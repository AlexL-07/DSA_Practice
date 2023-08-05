import modules
# to import a module use import file_name without the .py
import ecommerce.shipping
# when importing a package you put the folder name first, and then the file within that package that you want to import 
from ecommerce import shipping
# easier way to import all of the functions from a file within a package 
from modules import lbs_to_kg
# you can import specific functions by using from ... import ...
from ecommerce.shipping import calc_shipping
# to import a specific function from a file within a package 

print(modules.kg_to_lbs(43))
# by importing modules (the files name within the folder without the .py) you can access the functions on that file
# accessed by using module_name.function_name() 

print(lbs_to_kg(150))
# because this function was imported specifically it is not necessary to prefix it with the module name 

ecommerce.shipping.calc_shipping()
# using a function within a package 

calc_shipping()

shipping.calc_shipping()

# Python interpreter has a lot of built in modules if you want to learn about them go here: https://docs.python.org/3/py-modindex.html

import random
# random is an example of a module built into python, you can access random and its functions by importing it 
for i in range(3):
    print(random.random())
    # random.random() gives us a random float 
    print(random.randint(10, 20))
    # random.randint(a, b) gives a random number from within a-b inclusive 


members = ['Alex', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
    # random.choice(array) chooses an item randomly from a given array 
print(leader)

# there are a lot of other packages created by other python users online at https://pypi.org/