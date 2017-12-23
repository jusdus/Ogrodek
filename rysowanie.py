import pyglet


def przyczep_srodek(image):
    """Ustawia punkt obrotu na środek obrazka."""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


class ProbnyWyglad():
    wyglad = None

    def __init__(self):
        # to powinno być statyczne, bo jest wspólne dla wszystich instancji
        if ProbnyWyglad.wyglad is None:
            ProbnyWyglad.wyglad = pyglet.resource.image("Obrazki/probne.png")
            przyczep_srodek(ProbnyWyglad.wyglad)
        self.prezencja = pyglet.sprite.Sprite(img=ProbnyWyglad.wyglad)
        self.polozenie = 400
        self.szerokosc = 50

    def narysuj(self, poziom_ziemi):
        self.prezencja.position = (self.polozenie, poziom_ziemi)
        self.prezencja.scale = self.szerokosc / self.wyglad.width
        self.prezencja.draw()
        pass


def pokaz_ogrod(ogrod):
    # tworzy okno o podanej rozdzielczości
    win_size = (1280, 500)
    window = pyglet.window.Window(fullscreen=False, width=win_size[0], height=win_size[1])
    window.set_location((window.screen.width - win_size[0]) // 2, (window.screen.height - win_size[1]) // 2)

    rzeczy = []
    rzeczy.append(ProbnyWyglad())
    cos2 = ProbnyWyglad()
    cos2.szerokosc = 95
    cos2.polozenie = 100
    rzeczy.append(cos2)

    @window.event
    def on_draw():
        window.clear()
        for cos in rzeczy:
            cos.narysuj(300)

    pyglet.app.run()


pokaz_ogrod(None)
