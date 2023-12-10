# Dziedziczenie wielobazowe (diamond-shaped graphs)
# Wykorzystanie delegacji

class Animal:
    def __init__(self, name):
        print(name, 'is an animal.')


class Mammal(Animal):
    def __init__(self, name):
        print(name, 'is a warm-blooded animal.')
        Animal.__init__(self, name)


class NonWingedMammal(Mammal):
    def __init__(self, name):
        print(name, "can't fly.")
        Mammal.__init__(self, name)


class NonMarineMammal(Mammal):
    def __init__(self, name):
        print(name, "can't swim.")
        Mammal.__init__(self, name)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        NonMarineMammal.__init__(self, 'Dog')
        NonWingedMammal.__init__(self, 'Dog')


d = Dog()
