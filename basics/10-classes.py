
# Classes

## Simple Definitions

class Person:
    name = "Sarath"

    def getName(self):
        return self.name;

me = Person();
print(me.getName())


## Class init methos (constructor)

class Bear:

    name = "Teddy"

    def __init__(self):
        print("Class initializing",self.name);


t = Bear()
