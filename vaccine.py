import pygame
from pygame.sprite import Sprite 

class Vaccine(Sprite):
	"""a class to manage vaccines shot fromt the nurse"""
	def __init__(self, ai_game):
		"""create a vaccine object at the nurse's current position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.vaccine_color

		# Create a vaccine rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, self.settings.vaccine_width,
			self.settings.vaccine_height)
		self.rect.midtop = ai_game.nurse.rect.midtop
		self.rect.x = self.rect.x - 50

		# store the vaccine's position as a decimal value
		self.y = float(self.rect.y)
		

	def update(self):
		"""move the vaccine up the screen"""
		# update the decimal position of the vaccine
		self.y -= self.settings.vaccine_speed
		# update the rect position
		self.rect.y = self.y

	def draw_vaccine(self):
		"""draw the vaccine to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
