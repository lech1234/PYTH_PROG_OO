import datetime


class Osoba:
    """
    Klasa definiuje typ reprezentujący osobę.

    Umożliwia bezpośredni dostęp do atrybutów, co może doprowadzić do niespójności danych.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        """
        Metoda tworząca "publiczne" atrybuty instancyjne.
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec  # wartość logiczna: True - mężczyzna, False - kobieta
        self.rok_urodzenia = rok_urodzenia

    def podaj_plec(self):
        """
        Metoda zwraca informację o płci: M - mężczyzna, K - kobieta
        """
        return 'M' if self.plec else 'K'

    def ile_lat(self):
        """
        Metoda oblicza aktualny wiek osoby.
        """
        return datetime.date.today().year - self.rok_urodzenia

    def __str__(self):
        """
        Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
        Przykład:
        Jan Kowalski, płeć: M, wiek: 29 lat(a)
        """
        return f'{self.imie} {self.nazwisko}, płeć: {self.podaj_plec()}, wiek: {self.ile_lat()} lat(a)'


if __name__ == '__main__':

    # utworzenie osoby
    jk = Osoba('Jan', 'Kowalski', True, 1990)
    # sprawdzenie wartości atrybutów obiektu osoby
    print('IMIĘ:', jk.imie)
    print('NAZWISKO:', jk.nazwisko)
    print('KOMPLETNY OPIS:', jk, end='\n\n')

    # utworzenie osoby
    an = Osoba('Anna', 'Nowak', False, 2001)
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)

    # korekta roku urodzenia o 1 (odmłodzenie o 1 rok)
    an.rok_urodzenia += 1
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)

    # zmiana roku urodzenia na podaną wartość
    an.rok_urodzenia = 2025
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)
