import pyglet

class Ogrod:
    wyglad_ziemia = pyglet.resource.image("Obrazki/gleba.jpg")

    def __init__(self):
        self.rozmiar = 4
        self.rosliny = []

    def opis(self):
        lista = []
        for roslina in self.rosliny:
            lista.append("Roślina {0}".format(roslina))
        return "\n".join(lista)

    def pobliskie(self, uprawa):
        pass

    def zasadz(self, roslina, polozenie):
        self.rosliny.append(roslina)
        roslina.polozenie = polozenie
        pass

    def podlej(self, litry):
        # Rosliny.wilgotnosc += litry
        pass

    def czekaj(self, dni):
        # rozmiar ogrodu nie rośnie w czasie :)
        self.rozmiar += 2 * dni
        return self.rozmiar

    def pokaz(self, rozmiar_okna):
        poziom_ziemi = rozmiar_okna[1] // 2
        niebo = pyglet.image.SolidColorImagePattern((106, 166, 193, 255)).create_image(rozmiar_okna[0], rozmiar_okna[1])
        trawa = pyglet.image.SolidColorImagePattern((52, 115, 0, 255)).create_image(rozmiar_okna[0], 10)

        self.wyglad_ziemia.blit(0, 0)
        trawa.blit(0, poziom_ziemi)
        niebo.blit(0, poziom_ziemi + 10, 0)

        for ros in self.rosliny:
            ros.narysuj(1, poziom_ziemi) # TODO skala powinna być brana pod uwagę


if __name__ == "__main__":
    ogrod = Ogrod()
    marchewka = Roslina("marchewka")
    ogrod.zasadz(marchewka, 20)
    print(ogrod.opis())

