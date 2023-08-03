# try/except blocks 

try:
    age = int(input('Age: '))
        # because we are using int() here if we pass in characters that are not numbers python will normally throw an error of status code 1
    income = 20000
    risk = income / age 
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError: 
        # pass in whatever the error name you see in your terminal here, if you want that error to be excluded 
    print('Invalid Value')
        # by using except here instead of receiving an error we see the message "Invalid Value instead"