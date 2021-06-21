# create a class

# we name as Human
class Human:
    def __init__(self, name, age): # a constructor
        # define 2 attribute
        self.name = name
        self.age = age

    # define a method
    def greeting(self):
        print("Hello to", self.name, self.age)

if __name__ == "__main__":
    # create an object
    h1 = Human("Kimhan", 21)
    h1.greeting()

    # create another object
    h2 = Human("PP", 22)
    h2.greeting()