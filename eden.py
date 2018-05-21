from marchewka import Marchewka
import rysowanie
from ogrodek import Ogrod


def ask():
    print("Ile marchewek chcesz zasadzić?")
    many = int(input())
    ogrod = Ogrod()
    x = 100
    for i in range(many):
        ogrod.zasadz(Marchewka(), x)
        x += 100


if __name__ == "__main__":
    rysowanie.pokaz_ogrod(ogrod)

print(ask())




