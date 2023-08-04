# Class
class Point:
    # use uppercase letters to name a class and no underscores (pascal case)
    # Constructor
    def __init__(self, x, y):
        # this __init__ method is a constructor to create an object 
        self.x = x
        self.y = y


    def move(self):
        print("move")
    

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.draw()
# you can assign attributes to a class object:
# point1.x = 10
# point1.y = 20
print(point1.x)

class Person:
    def __init__(self, name):
        self.name = name

    
    def talk(self):
        print(f"Hi, I am {self.name}.")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

# Inheritance 

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    # ChildClass(ParentClass) for a class to inherit in python, you would pass in the parentclass to the childclass 
    def bark(self):
        print("bark")
    


class Cat(Mammal):
    pass
# pass will tell python interpreter to skip this line, because it gets mad when a class is empty 


cat1 = Cat()
cat1.walk()
dog1 = Dog()
dog1.bark()

