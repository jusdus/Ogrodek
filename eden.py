from marchewka import Marchewka
import rysowanie
from ogrodek import Ogrod
from uprawa import Uprawa

ogrod = Ogrod()
tury = 100


def wybor_rosliny():
    pass


def zasadzenie(roslina):
    print("Ile roślin chcesz zasadzić?")
    many = int(input())
    x = 100
    for r in ogrod.rosliny:
        x = max(x, r.polozenie + 100)
    for i in range(many):
        if roslina == "1":
            ogrod.zasadz(Marchewka(), x)
            x += 100


for i in range(1, tury+1):
    print("TURA {}".format(i))
    print("Wybierz akcję: \n(podlewanie - 1, sadzenie - 2, kolejna tura - 3, wyświetlanie stanu ogrodu - 4")
    akcja = int(input())
    if akcja not in range(1, 5):
        print("Błędna nazwa akcji")
    if akcja == 1:
        x = int(input("Podlać cały ogród (1) czy wybrać rośliny (2)"))
        if x == 1:
            pass
        elif x == 2:
            roslina = input(ogrod.rosliny)
        else:
            print("Wprowadzono błędną wartość")
    if akcja == 2:
        roslina = input("Proszę wybrać roślinę: marchewka (1)")
        zasadzenie(roslina)
        rysowanie.pokaz_ogrod(ogrod)
    if akcja == 3:
        i += 1
        if ogrod.rosliny:
            for r in ogrod.rosliny:
                r.rosnij(1)
    if akcja == 4:
        print(ogrod.opis())


