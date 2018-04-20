import pyglet

def przyczep_srodek(image):
    """Ustawia punkt obrotu na środek obrazka."""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2



def pokaz_ogrod(ogrod):
    win_size = (1280, 500)
    window = pyglet.window.Window(fullscreen=False, width=win_size[0], height=win_size[1])
    window.set_location((window.screen.width - win_size[0]) // 2, (window.screen.height - win_size[1]) // 2)

    @window.event
    def on_draw():
        window.clear()
        ogrod.pokaz(win_size)

    pyglet.app.run()



