# Arithmetic Operations
    # addition + 
    # subtraction - 
    # multiplication *
    # division /
        # gives a float (decimal) number
    # division //
        # gives a whole number 
    # modulo %
        # gives the remainder of a division 
    # exponentation, essentially this is 10^3 
print(10 ** 3)

# Operator Precedence 
    # parenthesis ()
    # exponentation **
    # multiplication *
    # division /
    # addition +
    # subtraction -

# Math Functions
x = 2.9
print(round(x))
    # rounds the number to its closest whole number 
print(abs(x))
    # returns the absolute value of a number, the return value is always going to be positive  

## Math Module
    # to access the math module and all of the functions associated with it you need to import math via import math 
import math
print(math.ceil(2.9))
    # math.ceil returns the ceiling of a number
        # in this case it would be 3
print(math.floor(2.9))
    # math.floor() returns the floor of a number 
        # in this case it would be 2
# many other functions within the math module, should look them up on my own
    # https://docs.python.org/3/library/math.html 