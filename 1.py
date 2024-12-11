class Czlowiek:
    l_ludzi = 0
    #Konstruktor - odpala sie w momencie tworzenia obiektu
    def __init__(self, imie, nazwisko, waga, zawod, wzrost, zarobki):
        Czlowiek.l_ludzi+= 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.zawod = zawod
        self.zarobki = zarobki

    def __str__(self):
        return 'imie: {}, nazwisko: {}, waga:{}, wzrost: {}, zawod: {}, zarobki:{}'.format(self.imie, self.nazwisko, self.waga,self.wzrost, self.zawod, self.zarobki)

    def rosnij_dzien(self):
        self.wzrost += 0.1


c1 = Czlowiek("Janusz", "Kowal", 100, "informatyk", 198, 25000)
"""print(c1.imie, c1.zawod, c1.wzrost)
print(c1)"""
print(c1)
c1.rosnij_dzien()
print(c1)

