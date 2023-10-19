from PPlay.window import *
from PPlay.sprite import *


def startgame():

    # Start resources
    gamewindow = Window(800, 600)
    gamewindow.set_background_color([0, 0, 0])

    teclado = gamewindow.get_keyboard()

    tiro_counter = 0 # Contador tiro

    # Player e tiros
    player = Sprite("game/nave.png")
    vel_player = 200
    player.set_position(gamewindow.width/2 - player.width/2, (gamewindow.height - player.height) - 10)

    vtiro = []
    vel_tiro = -500

    fundo = Sprite("game/game_fundo.png")

    # GameLoop
    while True:

        # Contadores
        tiro_counter += gamewindow.delta_time()

        if teclado.key_pressed("ESC"):
            break

        # Tiro
        if teclado.key_pressed("SPACE") and tiro_counter > 0.5:
            tiro = Sprite("game/tiro.png")
            tiro.set_position(player.x + player.width/2, player.y - tiro.height)
            vtiro.append(tiro)
            tiro_counter = 0

        for i in range(len(vtiro)):
            vtiro[i].move_y(vel_tiro * gamewindow.delta_time())
            if vtiro[i].y < 0 - vtiro[i].height:
                vtiro.pop(i)
                break


        # Movimento player
        player.move_key_x(vel_player * gamewindow.delta_time())

        if player.x < 0:
            player.x = 0
        elif player.x > gamewindow.width - player.width:
            player.x = gamewindow.width - player.width

        fundo.draw()
        player.draw()
        for i in range(len(vtiro)):
            vtiro[i].draw()
        gamewindow.update()
