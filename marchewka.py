#implementacja uprawy, podobnie jak probny wyglad, ale lepiej
#zasadzic w pliku rysowanie (napisac ogrodowi zasadz)

from rysowanie import przyczep_srodek
from ogrodek import Ogrod
from uprawa import Uprawa
import pyglet

class Marchewka(Uprawa):
    wyglad = None

    def __init__(self):
        super().__init__("Marchewka")
        self.waga = 1
        if Marchewka.wyglad is None:
            Marchewka.wyglad = pyglet.resource.image("Obrazki/marchewka.png")
            przyczep_srodek(Marchewka.wyglad)
        self.prezencja = pyglet.sprite.Sprite(img=Marchewka.wyglad)
        self.szerokosc = 50

    def narysuj(self, skala, poziom_ziemi):
        self.prezencja.position = (self.polozenie, poziom_ziemi)
        self.prezencja.scale = self.szerokosc / self.wyglad.width * skala
        self.prezencja.draw()
        pass

    def obszar(self):
        pass

    def podlej(self, litry):
        pass
