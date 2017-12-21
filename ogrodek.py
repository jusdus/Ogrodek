class Ogrod:
    def __init__(self):
        self.rozmiar = 4
        self.rosliny = []

    def opis(self):
        return "Rozmiar={0},Rosliny={1}".format(self.rozmiar, self.rosliny)

    def zasadz(self, roslina, polozenie):
        self.polozenie = 0
        pass

    def podlej(self, litry):
        #Rosliny.wilgotnosc += litry
        pass

    def czekaj(self, dni):
        self.rozmiar += 2*dni
        return self.rozmiar

    def pokaz(self):
        #pyglet

ogrod = Ogrod()
print(ogrod.opis())

