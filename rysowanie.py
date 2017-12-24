import pyglet

import ogrodek
import uprawa

def przyczep_srodek(image):
    """Ustawia punkt obrotu na środek obrazka."""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


class ProbnyWyglad():
    wyglad = None

    def __init__(self):
        # to powinno być statyczne, bo jest wspólne dla wszystich instancji
        if ProbnyWyglad.wyglad is None:
            ProbnyWyglad.wyglad = pyglet.resource.image("Obrazki/marchewka.png")
            przyczep_srodek(ProbnyWyglad.wyglad)
        self.prezencja = pyglet.sprite.Sprite(img=ProbnyWyglad.wyglad)
        self.polozenie = 400
        self.szerokosc = 50

    def narysuj(self, skala, poziom_ziemi):
        self.prezencja.position = (self.polozenie, poziom_ziemi)
        self.prezencja.scale = self.szerokosc / self.wyglad.width * skala
        self.prezencja.draw()
        pass


def pokaz_ogrod(ogrod):
    win_size = (1280, 500)
    window = pyglet.window.Window(fullscreen=False, width=win_size[0], height=win_size[1])
    window.set_location((window.screen.width - win_size[0]) // 2, (window.screen.height - win_size[1]) // 2)

    @window.event
    def on_draw():
        window.clear()
        ogrod.pokaz(win_size)

    pyglet.app.run()


if __name__ == "__main__":
    ogrod = ogrodek.Ogrod()
    ogrod.rosliny.append(ProbnyWyglad())
    pokaz_ogrod(ogrod)
