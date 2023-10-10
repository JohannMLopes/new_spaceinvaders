from PPlay.window import *


def startgame():

    # Start resources
    gamewindow = Window(800, 600)
    gamewindow.set_background_color([0, 0, 0])

    teclado = gamewindow.get_keyboard()


    while True:

        if teclado.key_pressed("ESC"):
            break

        gamewindow.update()
