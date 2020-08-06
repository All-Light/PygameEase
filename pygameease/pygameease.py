"""Main module."""


class Button:
	def __init__(self, x, y, width, height, color, highlight, text, text_color, outline_color, outline, outline_width,
				 x_resize, y_resize, width_resize, height_resize, running=True):
		# A lot of variables
		self.x = x  # X position of button. int
		self.y = y  # Y position of button. int
		self.width = width  # Width of button. int
		self.height = height  # Height of button. int
		self.color = color  # Default color of the button. (x,y,z)
		self.highlight = highlight  # Color of the button when hovered over. (x,y,z)
		self.text = str(text)  # The text to display on the button. Str
		self.rendered_text = ""  # The text rendered on the button. Str
		self.text_color = text_color  # Text color. (x,y,z)
		self.outline_color = outline_color  # The outline color. (x,y,z)
		self.outline = outline  # If you want an outline to the button or not. Boolean
		self.outline_width = outline_width  # Width of the outline, = 0 if no outline.  int
		
		# Resize works the same way as in the image class
		# Check the comments there for more info
		self.x_resize = x_resize  # E.g 3/10. float
		self.y_resize = y_resize  # E.g 199 / 201
		self.width_resize = width_resize  # E.g 1000/1004
		self.height_resize = height_resize  # E.g 1/2
		
		# An optional parameter needed to remove error
		self.running = running
	
	def draw(self, font, screen, pos, running=True):
		self.running = running
		
		# Checks if you want an outline and creates a different rect with the outline
		if self.outline:
			pygame.draw.rect(screen, self.outline_color, (
				self.x - self.outline_width, self.y - self.outline_width, self.width + 2 * self.outline_width,
				self.height + 2 * self.outline_width), 0)
		
		# Runs the is_over method and draws the button with highlight color
		if self.is_over(pos, running):
			pygame.draw.rect(screen, self.highlight, (self.x, self.y, self.width, self.height), 0)
		
		# Otherwise it draws the button with the default color
		else:
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
		
		# Makes sure that the text isn't empty
		if self.text != "":
			# This makes it possible to alter the text in the program by changing self.text
			self.rendered_text = self.text
			# Uses the font parameter to make the text into an actual text
			text = font.render(self.rendered_text, 1, self.text_color)
			# Draws the text in the middle of the button
			screen.blit(text, (
				self.x + int(self.width / 2 - text.get_width() / 2),
				self.y + int(self.height / 2 - text.get_height() / 2)))
	
	# draws the text in the middle of the button
	
	def resize(self, width, height):
		# resize takes the inputted resize "scale" from when the object was created and multiplies it by the new
		# width or height. This changes the values of the rect created in draw() and thus scales the whole button
		self.x = int(width * self.x_resize)
		self.y = int(height * self.y_resize)
		self.width = int(width * self.width_resize)
		self.height = int(height * self.height_resize)
	
	def is_over(self, pos, running):
		self.running = running
		
		# removes error in console
		if self.running:
			
			# gets the mouse position in a list consisting of the x-coordinate [0] and y-coordinate [1] and compares it
			# to the button
			if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
				return True  # returns True if mouse pos is over button
			
			# If not, it returns false
			return False
	
	def clicked(self, running, pos):
		# Checks if the mouse is over the button
		if self.is_over(running, pos):
			# Performs button specific action.
			# This action needs to be set after creation of the button.
			# This is done by first creating a definition for the action OUTSIDE this class.
			# Then you import types
			# Run the command "BUTTON_NAME_HERE.action = types.MethodType(DEFINITION_NAME_HERE, BUTTON_NAME_HERE)"
			# In your code after creating your button
			self.action()


class TextPrompt(Button):
	# It inherits all __init__ and the "is_over()" method from the button class
	def draw(self, font, screen, pos, running=True):
		self.running = running
		# The only difference in this method as opposed to the button class's method is the self.active part.
		# That part displays the default text if you have NOT clicked the prompt. Otherwise it is blank.
		if self.outline:  # checks if you want an outline.
			pygame.draw.rect(screen, self.outline_color, (
				self.x - self.outline_width, self.y - self.outline_width, self.width + 2 * self.outline_width,
				self.height + 2 * self.outline_width), 0)
		# creates outline according to the outline width
		
		if self.is_over(running, pos):  # checks if mouse is over button and changes color
			pygame.draw.rect(screen, self.highlight, (self.x, self.y, self.width, self.height), 0)
		
		else:  # else draw the prompt normally
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
		if not self.active:  # checks so that the prompt is not clicked and thus shows the default text
			self.rendered_text = self.text
			text = font.render(self.rendered_text, 1, self.text_color)
			screen.blit(text, (
				self.x + int(self.width / 2 - text.get_width() / 2),
				self.y + int(self.height / 2 - text.get_height() / 2)))
		
		if self.active:  # checks if the prompt is active and thus shows what the user has typed in
			text = font.render(self.rendered_text, 1, self.text_color)
			screen.blit(text, (
				self.x + int(self.width / 2 - text.get_width() / 2),
				self.y + int(self.height / 2 - text.get_height() / 2)))
	
	def clicked(self, running, pos):
		# The clicked() method does not perform an action in the prompt. Use an event chain in you main loop to create
		# characters to display in the font by changing,
		# "prompt.rendered_text = prompt.rendered_text + event.unicode" adds a character to the end of the text
		# "prompt.rendered_text = prompt.rendered_text[:-1]" removes a character at the end of the text
		# Perform "prompt.action()" when you have clicked "pygame.K_RETURN" aka the return/enter key
		
		if self.is_over(running, pos):  # checks if the user has clicked the prompt, inherited from button
			self.rendered_text = ""  # sets the text in the prompt to  nothing
			self.active = True  # sets the prompt to active mode
		
		# if user clicked anywhere but the prompt
		else:
			# make this prompt inactive
			self.active = False


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

