import pygame

pygame.init()


class Image:
	def __init__(self, x, y, width, height, image_source, scale_x=0, scale_y=0, scale_width=0, scale_height=0):
		# x = int. Desired picture x
		# y = int. Desired picture y
		# width = int. Desired picture width
		# height = int. Desired picture height
		# image_source = str. Where the picture is located
		#
		# All with the name "scale" are optional but required if you intend to run the resize command
		# This assumes the values are relative to the width or the height of the game window
		# If the x coordinate is determined by the width of the screen then E.g if x is determined by
		# "screen_width/2" then scale_x = 1/2. Eg 2, if x is determined by "3 * screen_width / 11", then scale_x = 3/11
		# scale_x = float.
		# scale_y = float.
		# scale_width = float.
		# scale_height = float.
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.image_source = image_source
		self.scale_x = scale_x
		self.scale_y = scale_y
		self.scale_width = scale_width
		self.scale_height = scale_height
		self.window_width = 0
		self.window_height = 0
		
		self.image = pygame.image.load(str(self.image_source))  # Loads the image from the image source
		self.image = pygame.transform.scale(self.image, (int(self.width), int(self.height)))

	def resize(self, new_width, new_height):
		# This method is run whenever the game window is rescaled.
		self.window_width = new_width
		self.window_height = new_height

		# You need to load the image again to prevent it from becoming pixelated by the resize
		self.image = pygame.image.load(str(self.image_source))
		self.image = pygame.transform.scale(self.image, (int(self.window_width * self.scale_width),
														int(self.window_height * self.scale_height)))
		self.x = int(self.window_width * self.scale_x)
		self.y = int(self.window_height * self.scale_y)
		self.width = int(self.window_width * self.scale_width)
		self.height = int(self.window_height * self.scale_height)
		
		