# Dziedziczenie wielobazowe (diamond-shaped graphs)
# Wykorzystanie funkcji super() w delegacji

class Animal:
    def __init__(self, name):
        print(name, 'is an animal.')


class Mammal(Animal):
    def __init__(self, name):
        print(name, 'is a warm-blooded animal.')
        super().__init__(name)


class NonWingedMammal(Mammal):
    def __init__(self, name):
        print(name, "can't fly.")
        super().__init__(name)


class NonMarineMammal(Mammal):
    def __init__(self, name):
        print(name, "can't swim.")
        super().__init__(name)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')


d = Dog()
