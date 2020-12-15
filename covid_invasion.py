import sys

import pygame

from settings import Settings
from nurse import Nurse
from vaccine import Vaccine 

class CovidInvasion(object):
	"""Overall class to manage game assets and behavior"""
	def __init__(self):
		super(CovidInvasion, self).__init__()

		pygame.init()
		self.settings = Settings()

		# self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption("COVID Invasion")

		self.nurse = Nurse(self)
		self.vaccines = pygame.sprite.Group()


	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.nurse.update()
			self._update_vaccines()
			self._update_screen()			

			# make the most recently drawn screen visible
			pygame.display.flip()

	def _check_events(self):
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""respond to key presses"""
		if event.key == pygame.K_RIGHT:
			self.nurse.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.nurse.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_vaccine()

	def _check_keyup_events(self, event):
		"""respond to key releases"""
		if event.key == pygame.K_RIGHT:
			self.nurse.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.nurse.moving_left = False

	def _fire_vaccine(self):
		"""create a new vaccine and add it to the vaccines group"""
		if len(self.vaccines) < self.settings.vaccines_allowed:
			new_vaccine = Vaccine(self)
			self.vaccines.add(new_vaccine)

	def _update_screen(self):
		# redraw the screen
		self.screen.fill(self.settings.bg_color)
		self.nurse.blitme()
		for vaccine in self.vaccines.sprites():
			vaccine.draw_vaccine()

	def _update_vaccines(self):
		"""update position of vaccines and get rid of old vaccines"""
		self.vaccines.update()

		# get rid of vaccines that have disappeared
		for vaccine in self.vaccines.copy():
			if vaccine.rect.bottom <= 0:
				self.vaccines.remove(vaccine)

if __name__ == '__main__':
	# make a game instance, and run the game
	ai = CovidInvasion()
	ai.run_game()
		