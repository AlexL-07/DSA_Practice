# if/elif/else
is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
    # whatever is indented under the if/elif/else statement will run if it is true
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day") 

print("Enjoy your day")
# because this line isn't indented it will run regardless of condition, pretty much functions outside of the conditionals

# Logical Operators
    # and: both conditions has to be true
    # or: at least one condition has to be true
    # not: converts a boolean value to its opposite value
has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit: 
    print("Eligible for loan 1")

if has_good_credit or has_high_income:
    print("Eligile for loan 2")

if has_good_credit and not has_criminal_record:
    print("Eligile for loan 3")

# Comparison Operators
    # == : equal
    # != : not equal 
    # > : greater than
    # < : less than
    # >= : greater than or equal to 
    # <= : less than or equal to 