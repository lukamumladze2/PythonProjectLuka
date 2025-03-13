class Cat:

    def eat(self):
        return "cat drinks milk"
    def talk(self):
        return "cat says Meoww"
    def walk(self):
        return "cat can run 20km/h"

class Dog:

    def eat(self):
        return "Dog eats a bone"
    def talk(self):
        return "Dog says awww"
    def walk(self):
        return "Dog can run 40km/h"

c1 = Cat()
print(c1.eat())
print(c1.talk())
print(c1.walk())
d1 = Dog()
print(d1.eat())
print(d1.talk())
print(d1.walk())