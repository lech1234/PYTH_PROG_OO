import datetime


class Osoba:
    """
    Klasa definiuje typ reprezentujący osobę.

    Klasa wykorzystuje właściwości. Do ich implemntacji użyto funkcji property.
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
    def __podaj_imie(self):
        return self.__imie

    def __podaj_nazwisko(self):
        return self.__nazwisko

    def __podaj_plec(self):
        return 'M' if self.__plec else 'K'

    def __podaj_rok_urodzenia(self):
        return self.__rok_urodzenia

    # metody dostępowe do ustawiania atrybutów (settery)

    def __ustaw_imie(self, imie):
        if imie:
            self.__imie = imie
        else:
            print('....... Zmiana imienia odrzucona (imię nie może być puste)')

    def __ustaw_nazwisko(self, nazwisko):
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            print('....... Zmiana nazwiska odrzucona (nazwisko nie może być puste)')

    def __ustaw_plec(self, plec):
        if isinstance(plec, bool):
            self.__plec = plec
        else:
            print('....... Zmiana płci odrzucona (płeć musi być wartością typu logicznego')

    def __ustaw_rok_urodzenia(self, rok_urodzenia):
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            print('....... Zmiana roku urodzenia odrzucona (rok jeszcze nie nadszedł)')

    # utworzenie właściwości
    imie = property(__podaj_imie, __ustaw_imie)
    nazwisko = property(__podaj_nazwisko, __ustaw_nazwisko)
    plec = property(__podaj_plec, __ustaw_plec)
    rok_urodzenia = property(__podaj_rok_urodzenia, __ustaw_rok_urodzenia)

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
        return f'{self.__imie} {self.__nazwisko}, płeć: {self.__plec}, wiek: {self.ile_lat()} lat(a)'


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
