class Settings:
	"""A class to store all the settings for Covid Invasion"""
	def __init__(self):
		super(Settings, self).__init__()
		# screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)

		# nurse settings
		self.nurse_speed = 1.5
		