import pyglet

window = pyglet.window.Window(width=640, height=480)

@window.event
def on_draw():
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (10, 15, 30, 35))
    )
on_draw()