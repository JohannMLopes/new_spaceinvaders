import game
import menu_diff
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

# Start resources
menuwindow = Window(800, 600)
menuwindow.set_title("Space Invaders")

mouse = menuwindow.get_mouse()

dificuldade = 1

# Start menu

play = Sprite("menu/start.png")
diff = Sprite("menu/dificuldade.png")
ranking = Sprite("menu/ranking.png")
sair = Sprite("menu/sair.png")
fundo = GameImage("menu/fundo.png")

sair.x = menuwindow.width/2 - sair.width/2
sair.y = menuwindow.height - sair.height - 50

ranking.x = menuwindow.width/2 - ranking.width/2
ranking.y = sair.y - ranking.height - 25

diff.x = menuwindow.width/2 - diff.width/2
diff.y = ranking.y - diff.height - 25

play.x = menuwindow.width/2 - play.width/2
play.y = diff.y - play.height - 25

# Loop
while True:

    if mouse.is_over_area([diff.x, diff.y], [diff.x + diff.width, diff.y + diff.height]) and mouse.is_button_pressed(1):
        dificuldade = menu_diff.setdificuldade()

    elif mouse.is_over_area([play.x, play.y], [play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
        game.startgame(dificuldade)

    elif mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
        break

    fundo.draw()
    play.draw()
    diff.draw()
    ranking.draw()
    sair.draw()
    menuwindow.draw_text("%.1f" % dificuldade, menuwindow.width - 100, menuwindow.height - 100, 24, [0, 0, 0], "Arial", False, False)
    menuwindow.update()
