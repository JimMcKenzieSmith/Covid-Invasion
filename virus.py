import pygame
from pygame.sprite import Sprite 

class Virus(Sprite):
	"""a class to represent a single virus in the fleet"""
	def __init__(self, ai_game):
		"""initialize the virus and set its starting position"""
		super().__init__()
		self.screen = ai_game.screen

		# load the virus image and set its rect attribute
		self.image = pygame.image.load('images/virus.png')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()

		# start each new virus near the3 top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store the virus' exact horizontal position
		self.x = float(self.rect.x)
		