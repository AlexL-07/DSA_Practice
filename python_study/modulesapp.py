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