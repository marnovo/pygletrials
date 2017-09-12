# Pysteroids

import pyglet
import resources

game_window = pyglet.window.Window(width=800, height=600)
if __name__ == '__main__':
    pyglet.app.run()

score_label = pyglet.text.Label(text="score: 0", x=10, y=575)
level_label = pyglet.text.Label(text="Pysteroids", x=400, y=575, anchor_x='center')
player_ship = pyglet.sprite.Sprite(img=resources.player_img, x=400, y=300)


@game_window.event
def on_draw():
    game_window.clear()
    level_label.draw()
    score_label.draw()
    player_ship.draw()
