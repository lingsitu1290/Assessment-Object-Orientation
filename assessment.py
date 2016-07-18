"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Encapsulation, abstraction, and polymorphism. 

2. What is a class?
   Class is a type of thing. 

3. What is an instance attribute?
    A characteristic that is specific to that individual instance of a class. 

4. What is a method?
    A method is a function within a class. 

5. What is an instance in object orientation?
    An instance is a specific instance of a class. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is a characteristic that is specific to the whole class (
    or every instance of that class). An instance attribute is a characteristic
    that is specific to that instance of the class.

    For example, in a Dog Class. A class attribute that the species of this class 
    is set is Dog since the species of this class is Dog fo all instances. 

    An instance attribute in our Dog Class can be name. For each dog, each will have 
    a different name.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Liquid(object):

    def __init__(self, drinkable, flavor):
        self.drinkable = drinkable
        self.flavor = flavor

    def get_info(self, name):
        self.name = name
        return self.name


class Coffee(Liquid):
    drinkable = True

    def add_milk(self):
        self.milk = True
        return self.milk


latte = Coffee(True, 'Strawberry')
print latte.flavor
print latte.get_info('latte')
print latte.drinkable
print latte.add_milk()
