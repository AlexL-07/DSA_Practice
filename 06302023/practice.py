print("hello world")
birth_year = input('Birth year: ')
    ## input() takes in a user's input, they can type this in the terminal for now 
age = 2023 - int(birth_year)
## int() converts a string into an integer
## other type conversions: 
    ## bool()
    ## float()
## type() can be used to check what class something is i.e., str, int, etc. 
print(age)