from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *


def setdificuldade():

    # Start resources
    dificuldadewindow = Window(800, 600)

    mouse = dificuldadewindow.get_mouse()

    fundo = GameImage("menu/fundo.png")
    facil = Sprite("menu/facil.png")
    medio = Sprite("menu/medio.png")
    dificil = Sprite("menu/dificil.png")

    dificil.x = dificuldadewindow.width / 2 - dificil.width / 2
    dificil.y = dificuldadewindow.height - dificil.height - 50

    medio.x = dificuldadewindow.width/2 - medio.width/2
    medio.y = dificil.y - medio.height - 25

    facil.x = dificuldadewindow.width/2 - facil.width/2
    facil.y = medio.y - facil.height - 25

    # Loop
    while True:
        if mouse.is_over_area([facil.x, facil.y], [facil.x + facil.width, facil.y + facil.height]) and mouse.is_button_pressed(1):
            diff = 1
            return diff
        if mouse.is_over_area([medio.x, medio.y], [medio.x + medio.width, medio.y + medio.height]) and mouse.is_button_pressed(1):
            diff = 1.5
            return diff
        if mouse.is_over_area([dificil.x, dificil.y], [dificil.x + dificil.width, dificil.y + dificil.height]) and mouse.is_button_pressed(1):
            diff = 2
            return diff

        fundo.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
        dificuldadewindow.update()
