class Samochod:
    l_pojazdow = 0
    def __init__(self, numer, miejsca, marka, bak, spalanie, przebieg, paliwo, wlasciciel, ubezpieczenie, adres):
        Samochod.l_pojazdow +=1
        self.numer = numer
        self.miejsca = int(miejsca)
        self.marka = marka
        self.bak = float(bak)
        self.spalanie = float(spalanie)
        self.przebieg = float(przebieg)
        self.paliwo = float(paliwo)
        self.wlasciciel = wlasciciel
        self.ubezpieczenie = ubezpieczenie
        self.adres = adres


    def __str__(self):
        return 'numer: {}, miejsca:{}, marka:{}, bak:{}, spalanie:{}, przebieg:{}, paliwo:{}, wlasciciel:{}, ubezpieczenie:{}, adres:{}'.format(self.numer, self.miejsca, self.marka, self.bak, self.spalanie, self.przebieg, self.przebieg, self.paliwo, self.wlasciciel, self.ubezpieczenie, self.adres)


    def nadaj_wlasciciela(self):
        self.wlasciciel = input("Podaj imie i nazwisko wlasciciela: ")
        self.adres = input("Podaj adres: ")

    def przypisz_ubezpieczenie(self):
        self.ubezpieczenie = input("Podaj numer ubezpieczenia pojazdu:")

    def informacje_podstawowe(self):
        

    def przejedz(self):


    def uzupelnij_paliwo(self):






s1 = Samochod('1234567893', '6', 'Audi', '9.6', '4.8', '200000.0', '7.5', 'Mariusz Bąk', 'u04', 'Kanarkowa 77')
s1.nadaj_wlasciciela()
print(s1)