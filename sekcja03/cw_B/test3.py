"""
Porównanie dwóch instancji tej samej klasy o tym samym stanie daje True.
Instancje są haszowalne.
"""
import typing


class Schowek:
    def __init__(self, wartosc):
        self.__wartosc = wartosc

    def __eq__(self, other):
        if self.__class__ == other.__class__ and self.__wartosc == other.__wartosc:
            return True
        return False

    def __hash__(self):
        return hash(self.__wartosc)


if __name__ == '__main__':
    s1 = Schowek(1)
    s2 = Schowek(1)

    czy_rowne = s1 == s2
    print(f'Czy s1 i s2 są równe? {"tak" if czy_rowne else "nie"}')

    czy_haszowalne = isinstance(s1, typing.Hashable) and isinstance(s2, typing.Hashable)
    print(f'\nCzy s1 i s2 są haszowalne? {"tak" if czy_haszowalne else "nie"}')

    if czy_haszowalne:
        print(f'hash(s1) = {hash(s1)}')
        print(f'hash(s2) = {hash(s2)}')
