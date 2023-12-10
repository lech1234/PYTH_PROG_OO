import datetime


class Osoba:
    """
    Klasa definiuje typ reprezentujący osobę.

    Klasa wykorzystuje właściwości. Do ich implementacji użyto dekoratorów.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        """
        Metoda inicjująca właściwości.
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.rok_urodzenia = rok_urodzenia

    # Metody dostępowe do odczytu atrybutów (gettery)
    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def plec(self):
        return 'M' if self.__plec else 'K'

    @property
    def rok_urodzenia(self):
        return self.__rok_urodzenia

    # Metody dostępowe do ustawiania atrybutów (settery)

    @imie.setter
    def imie(self, imie):
        if imie:
            self.__imie = imie
        else:
            print('....... Zmiana imienia odrzucona (imię nie może być puste)')

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            print('....... Zmiana nazwiska odrzucona (nazwisko nie może być puste)')

    @plec.setter
    def plec(self, plec):
        if isinstance(plec, bool):
            self.__plec = plec
        else:
            print('....... Zmiana płci odrzucona (płeć musi być wartością typu logicznego')

    @rok_urodzenia.setter
    def rok_urodzenia(self, rok_urodzenia):
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            print('....... Zmiana roku urodzenia odrzucona (rok jeszcze nie nadszedł)')

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
        return f'{self.imie} {self.nazwisko}, płeć: {self.plec}, wiek: {self.ile_lat()} lat(a)'


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

    # zmiana roku urodzenia o 1 (odmłodzenie)
    an.rok_urodzenia += 1
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)

    # korekta roku urodzenia o 1 (odmłodzenie o 1 rok)
    an.rok_urodzenia = 2025
    # sprawdzenie wartości atrybutów obiektu osoby
    print('KOMPLETNY OPIS:', an)
