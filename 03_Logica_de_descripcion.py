from owlready2 import *

onto = get_ontology("http://example.org/animals.owl")

with onto:
    class Animal(Thing):
        pass

    class Carnivore(Animal):
        pass

john = Animal()
john.name = "John"

print(john.is_a)
