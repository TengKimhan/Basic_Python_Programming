# inhertance mean inherit from another class

# base class
class Animal():
    def eat(self):
        print("I can eat")

    def drink(self):
        print("I can drink")

# the class that inherit from base class
class Panda(Animal):
    def __init__(self):
        self.eat()
        self.drink()

    def inro(self):
        print("I am", "Panda")
        print("Height:", 12)
        print("Weight:", 12)

panda = Panda()
panda.inro()

# check isinstance() and issubclass()
# Actually, panda is an instance of class Panda
# class Panda is a subclass of Animal
print(isinstance(panda, Panda))
print(issubclass(Panda, Animal))