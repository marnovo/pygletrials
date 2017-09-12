import pyglet

# Initialize pyglet's resources
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# Set images for assets
player_image = pyglet.resource.image("player.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")


def center_image(image):
    """Anchor images to their center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)
