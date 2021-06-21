class Father:
    def skills(self):
        print("I am gardening")

class Mother:
    def skills(self):
        print("I am cooking")

# class that inherit from Mother and Father
class Child(Mother, Father):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I like sport")

# create an object
c = Child()
c.skills()

# check
print("c is an instance of Child:", isinstance(c, Child))
print("Child is a subclass of Mother:", issubclass(Child, Mother))
print("Child is a subclass of Father:", issubclass(Child, Father))