class Uprawa:
    def __init__(self, nazwa):
        self.ogrod = None  # przy sadzeniu zostanie ustawiony przez ogrod
        self.nazwa = nazwa
        self.waga = 0
        self.wilgotnosc = 0.0
        self.wiek = 0
        self.polozenie = 0

    def rosnij(self, dni):
        # możemu tutaj zmienić wiek uprawy, bo to niezależy od jej rodzaju
        pass

    def podlej(self, litry):
        pass

    def opis(self):
        # można stworzyć opis z tego co już mamy
        pass

    def obszar(self):
        #rectangle
        pass

    def narysuj(self):
        #pyglet
        pass
