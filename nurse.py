import pygame

class Nurse:
	""" A class for the nurse. """

	def __init__(self, ai_game):
		"""Initialize the nurse and set her starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# load the nurse image and get its rect
		self.image = pygame.image.load('images/nurse.gif')
		self.image = pygame.transform.scale(self.image, (150, 150))
		self.rect = self.image.get_rect()

		# start each new nurse at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# store decimal value for nurse's horizontal position
		self.x = float(self.rect.x)

		# movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update the nurse's position based on the movement flag"""
		if self.moving_right:
			self.x += self.settings.nurse_speed
		if self.moving_left:
			self.x -= self.settings.nurse_speed

		# update rect object from self.x
		self.rect.x = self.x

	def blitme(self):
		"""draw the nurse at its current location"""
		self.screen.blit(self.image, self.rect)
