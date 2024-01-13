"""
Porównanie dwóch instancji tej samej klasy o tym samym stanie daje False.
Instancje są haszowalne.
"""
import typing


class Schowek:
    def __init__(self, wartosc):
        self.__wartosc = wartosc


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
