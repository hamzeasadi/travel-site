import pyglet
import numpy as np

class Window(pyglet.window.Window):
	
	def __init__(self):
		super().__init__()
		self.set_size(600,600)

	def on_draw(self):
		self.clear()
		pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES, [0, 1, 2], ('v2i', (300, 300, 300, 350, 350, 300)))

if __name__ == '__main__':
	window = Window()
	pyglet.app.run()

	
