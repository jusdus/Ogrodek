class Roslina():
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.waga = 0
        self.wilgotnosc = 0.0
        self.wiek = 0
        self.polozenie = 0

    def rosnij(self, dni):
        self.wiek += dni
        self.waga += dni*2
        self.wilgotnosc -= 0.1*self.wilgotnosc
        if self.wiek > 100:
            return "czas na zbiory"
        elif self.wiek >= 70:
            return "wkrotce zbiory"
        elif self.wiek >= 40:
            return "jeszcze dużo czasu"
        else:
            return "świeżo zasiane!"

    def podlej(self, litry):
        self.wilgotnosc += litry

    def opis(self):
        return "{} waży {} gram i ma {} dni. \n Wilgotność: {}\n Położenie: {}".format(self.nazwa, self.waga, self.wiek, self.wilgotnosc, self.polozenie)

    def obszar(self):
        self.x = 6
        self.y = 4
        pass

    def rysuj(self):
        pass


marchewka = Roslina("Marchewka")
dab = Roslina("Dąb")
dab.rosnij(20)

if __name__ == "__main__":
    print(marchewka.rosnij(20))
    print(marchewka.opis())
    print(dab.opis())



