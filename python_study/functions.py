# Functions 

def greet_user(first_name, last_name):
    print(f"Hi there {first_name} {last_name}!")
    print(f"Welcome aboard {first_name}")
    # whatever is indented following def function_name(): is a part of this function, 
    # anything not indented under the function will be considered outside of it 


# whenever you define a function you should add 2 line breaks after the end of the function  
greet_user("Alex", "Luong")
    # you can call a function like so
    # for functions in python you can pass in parameters through the parentheses following the function's name
    # if the function has a parameter and you do not pass in an argument python will throw an error  
greet_user("Mary", "Smith")
    # an example of positional arguments
greet_user(last_name="Smith", first_name="John")
    # this is how you would pass in keyword arguments, by assigning the desired string to the correct parameter from the function
greet_user("John", last_name="Smith")  
    # if you want to use keyword arguments with positional arguments make sure to use the keyword argument AFTER the positional argument



# Return Statement
def square(n):
    return n * n 


# return statements gives the user of the function a value after executing the function, without a return function the user won't receive anything back from the function
# by default in python the return of a function will be None
print(square(10))
    # you have to print the return value to see it in the terminal






     

