import pyglet

# Initialize pyglet's resources
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# Set images for assets
player_img = pyglet.resource.image("man.png")
rain_img = pyglet.resource.image("man.png")


def center_image(image):
    """Anchor images to their center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Center all image anchors
center_image(player_img)
center_image(rain_img)
