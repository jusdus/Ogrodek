class Ogrod:
    def __init__(self):
        self.rozmiar = 4
        self.rosliny = []

    def opis(self):
        return "Rozmiar={0},Rosliny={1}".format(self.rozmiar, self.rosliny)

ogrod = Ogrod()
print (ogrod.opis())

