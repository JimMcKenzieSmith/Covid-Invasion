import sys

import pygame

from settings import Settings
from nurse import Nurse

class CovidInvasion(object):
	"""Overall class to manage game assets and behavior"""
	def __init__(self):
		super(CovidInvasion, self).__init__()

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("COVID Invasion")

		self.nurse = Nurse(self)


	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.nurse.update()
			self._update_screen()			

			# make the most recently drawn screen visible
			pygame.display.flip()

	def _check_events(self):
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.nurse.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.nurse.moving_left = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.nurse.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.nurse.moving_left = False

	def _update_screen(self):
		# redraw the screen
		self.screen.fill(self.settings.bg_color)
		self.nurse.blitme()


if __name__ == '__main__':
	# make a game instance, and run the game
	ai = CovidInvasion()
	ai.run_game()
		