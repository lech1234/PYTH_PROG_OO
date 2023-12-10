import datetime


class Osoba:
    """
    Klasa definiuje typ reprezentujący osobę.

    Klasa jest shermetyzowana.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        """
        Metoda tworząca "silnie prywatne" atrybuty instancyjne.
        """
        self.ustaw_imie(imie)
        self.ustaw_nazwisko(nazwisko)
        self.ustaw_plec(plec)
        self.ustaw_rok_urodzenia(rok_urodzenia)

    # Metody dostępowe do odczytu atrybutów (gettery)
    def podaj_imie(self):
        """
        Metoda zwraca imię osoby.
        """
        return self.__imie

    def podaj_nazwisko(self):
        """
        Metoda zwraca nazwisko osoby.
        """
        return self.__nazwisko

    def podaj_plec(self):
        """
        Metoda zwraca informację o płci: M - mężczyzna, K - kobieta
        """
        return 'M' if self.__plec else 'K'

    def podaj_rok_urodzenia(self):
        """
        Metoda zwraca rok urodzenia osoby.
        """
        return self.__rok_urodzenia

    # metody dostępowe do ustawiania atrybutów (settery)
    def ustaw_imie(self, imie):
        """
        Metoda zmienia imię, o ile nowe imię nie jest pustym tekstem.
        """
        if imie:
            self.__imie = imie
        else:
            print('....... Zmiana imienia odrzucona (imię nie może być puste)')

    def ustaw_nazwisko(self, nazwisko):
        """
        Metoda zmienia nazwisko, o ile nowe nazwisko nie jest pustym tekstem.
        """
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            print('....... Zmiana nazwiska odrzucona (nazwisko nie może być puste)')

    def ustaw_plec(self, plec):
        """
        Metoda zmienia płeć, o ile nowa płeć jest wartością typu logicznego.
        """
        if isinstance(plec, bool):
            self.__plec = plec
        else:
            print('....... Zmiana płci odrzucona (płeć musi być wartością typu logicznego')

    def ustaw_rok_urodzenia(self, rok_urodzenia):
        """
        Metoda zmienia rok urodzenia, o ile już nadszedł.
        """
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            print('....... Zmiana roku urodzenia odrzucona (rok jeszcze nie nadszedł)')

    def ile_lat(self):
        """
        Metoda oblicza aktualny wiek osoby.
        """
        return datetime.date.today().year - self.__rok_urodzenia

    def __str__(self):
        """
        Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
        Przykład:
        Jan Kowalski, płeć: M, wiek: 29 lat(a)
        """
        return f'{self.__imie} {self.__nazwisko}, płeć: {self.podaj_plec()}, wiek: {self.ile_lat()} lat(a)'


if __name__ == '__main__':
    # utworzenie osoby
    jk = Osoba('Jan', 'Kowalski', True, 1990)
    # sprawdzenie wartości atrybutów obiektu osoby
    print('IMIĘ:', jk.podaj_imie())
    print('NAZWISKO:', jk.podaj_nazwisko())
    print('KOMPLETNY OPIS:', jk, end='\n\n')

    # utworzenie osoby
    an = Osoba('Anna', 'Nowak', False, 2001)
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)

    # korekta roku urodzenia o 1 (odmłodzenie o 1 rok)
    an.ustaw_rok_urodzenia(an.podaj_rok_urodzenia() + 1)  # wygląda koszmarnie...
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)

    # zmiana roku urodzenia na podaną wartość
    an.ustaw_rok_urodzenia(2025)
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)
