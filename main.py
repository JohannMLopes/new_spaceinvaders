import game
import menu_diff
from PPlay.window import *
from PPlay.sprite import *

# INICIA RECURSOS
menuwindow = Window(800, 600)
menuwindow.set_title("Space Invaders")

mouse = menuwindow.get_mouse()

dificuldade = 1

# INICIA OPÇOES MENU

play = Sprite("menu/play.png")
diff = Sprite("menu/diff.png")
ranking = Sprite("menu/rank.png")
sair = Sprite("menu/exit.png")

play.x = 50
play.y = 20

diff.x = 50
diff.y = play.y + diff.height + 20

ranking.x = 50
ranking.y = diff.y + ranking.height + 20

sair.x = 50
sair.y = ranking.y + sair.height + 20

# GAMELOOP
while True:

    if mouse.is_over_area([diff.x, diff.y], [diff.x + diff.width, diff.y + diff.height]) and mouse.is_button_pressed(1):
        dificuldade = menu_diff.setdificuldade()

    if mouse.is_over_area([play.x, play.y], [play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
        game.startgame()

    if mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
        break

    menuwindow.set_background_color([255, 255, 255])
    play.draw()
    diff.draw()
    ranking.draw()
    sair.draw()
    menuwindow.draw_text("%.1f" % dificuldade, 400, 50, 24, [0, 0, 0], "Arial", False, False)
    menuwindow.update()
