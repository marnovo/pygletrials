# Raining man

import pyglet
import random
from pyglet.window import key
import resources

game_window = pyglet.window.Window(width=640, height=480)
player = resources.player_img
rain = resources.rain_img


class Game(object):
    def __init__(self):
        self.player_x = game_window.width // 2
        self.player_y = 0 + - resources.player_img.height // 2
        self.rain_x = game_window.width // 2
        self.rain_y = game_window.height
        self.score = 0
        self.gameover = False


game = Game()

score_label = pyglet.text.Label(str(game.score),
                                x=game_window.width // 2,
                                y=game_window.height // 2,
                                anchor_x='center',
                                anchor_y='center')


@game_window.event
def on_key_press(symbol, modifiers):
    """ Controls on key press event """
    if symbol == key.RIGHT:
        game.player_x += 15
    elif symbol == key.LEFT:
        game.player_x -= 15


@game_window.event
def on_draw():
    """ Sprite update on image draw """
    if not game.gameover:
        game_window.clear()
        player.blit(game.player_x, game.player_y)
        rain.blit(game.rain_x, game.rain_y)
        score_label.text = str(game.score)
        score_label.draw()
    else:
        game_window.clear()
        score_label.text = 'Game Over\nScore: %d' % game.score
        score_label.draw()


def rain_drop(dt):
    """ Check for collisions """
    # Did it collide
    if (abs(game.rain_x - game.player_x) < 40
       and abs(game.rain_y - game.player_y) < 40):
        game.gameover = True
        return

    # New rain drop
    if game.rain_y <= 10:
        game.rain_x = random.randint(0, game_window.width)
        game.rain_y = game_window.height
        game.score += 1
    else:
        game.rain_y -= 3


pyglet.clock.schedule(rain_drop)
pyglet.app.run()
