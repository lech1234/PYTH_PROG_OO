class Pracownik:
    def __init__(self, imie, nazwisko, zarobki):
        """
        Metoda tworząca atrybuty instancyjne.
        """
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__zarobki = zarobki

    def __str__(self):
        """
        Metoda konwersji obiektu pracownika na postać tekstową (zwraca pełny opis obiektu)
        Przykład:
        [Pracownik] Jan Kowalski, zarobki: 4000
        """
        return f'[{self.__class__.__name__}] {self.__imie} {self.__nazwisko}, zarobki: {self.__zarobki}'


class KierownikZespolu(Pracownik):
    def __init__(self, imie, nazwisko, zarobki, odpowiedzialnosc):
        """
        Metoda tworząca atrybuty instancyjne.
        """
        super().__init__(imie, nazwisko, zarobki)
        self.__lista_pracownikow = []
        self.__odpowiedzialnosc = odpowiedzialnosc

    def dodaj_pracownika(self, pracownik):
        """
        Metoda dodaje pracownika do zespołu.
        """
        if not pracownik in self.__lista_pracownikow:
            self.__lista_pracownikow.append(pracownik)

    def usun_pracownika(self, pracownik):
        """
        Metoda usuwa pracownika z zespołu.
        """
        if pracownik in self.__lista_pracownikow:
            self.__lista_pracownikow.remove(pracownik)

    def kto_w_zespole(self):
        print('ZESPÓŁ:')
        print(*self.__lista_pracownikow, sep='\n')

    def __str__(self):
        """
        Metoda konwersji obiektu kierownika zespołu na postać tekstową (zwraca pełny opis obiektu)
        Przykład:
        [KierownikZespolu] Tomasz Nowak, zarobki: 7000, odpowiedzialność: kierownik projektu w Pythonie
        """
        return super().__str__() + f', odpowiedzialność: {self.__odpowiedzialnosc}'


if __name__ == '__main__':

    p1 = Pracownik('Jan', 'Kowalski', 4_000)
    p2 = Pracownik('Tomasz', 'Jabłoński', 4_000)
    kz1 = KierownikZespolu('Tomasz', 'Nowak', 7_000, 'kierownik projektu w Pythonie')

    print(p1)
    print(p2)
    print(kz1)
    kz1.kto_w_zespole()

    kz1.dodaj_pracownika(p1)
    kz1.dodaj_pracownika(p2)
    kz1.kto_w_zespole()

    kz1.usun_pracownika(p1)
    kz1.kto_w_zespole()
