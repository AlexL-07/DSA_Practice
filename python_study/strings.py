# Strings
string = 'Hello World'

# String Indexing
print(string[0])
    # this gives the first index of the string
print(string[-1])
    # this gives the last index of the string
print(string[0:3])
    # this gives all the indexes from 0-2, excluding index 3 
print(string[0:])
    # this gives the entire string
print(string[1:])
    # this gives the entire string starting from index 1
    # when an index is left blank in these ranges, the first blank space is assumed to be 0 and the second blank space is assumed to be -1 


# Formatting String
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder.'
    # By prefixing your strings with f'' you can use {} on your variables to format a string
        # allowing you to use your variables as a placeholder for their values in your string 

print(message)
print(msg)


# String Methods
course = 'Python for Beginners'
print(len(course))
    # len(string) gives us the length of a string 
print(course.upper())
    # string.upper() makes every character of a string uppercase 
print(course.lower())
    # string.lower() makes every character of a string lowercase 
print(course.find('P'))
    # string.find('') finds the first index where the specified character appears in your string
        # case sensitive
        # if the character is not within the string it will return -1 
        # can be used with entire strings to find the first index where that string appears 
print(course.replace('Beginners', 'Noobs'))
    # string.replace('string1, string2') finds and replaces string1 with string2 
print('Python' in course)
    # 'input string' in 'string' searches for the input string within the string and returns a boolean  
  

