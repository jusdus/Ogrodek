from marchewka import Marchewka
import rysowanie
from ogrodek import Ogrod


if __name__ == "__main__":
    ogrod = Ogrod()
    ogrod.zasadz(Marchewka(),400)
    ogrod.zasadz(Marchewka(),200)
    ogrod.zasadz(Marchewka(),300)
    rysowanie.pokaz_ogrod(ogrod)