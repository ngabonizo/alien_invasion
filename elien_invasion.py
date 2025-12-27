import sys
import pygame
from settings import Settings
class ElienInvasion:
  # Overall class to manage game behavior

  def __init__(self):
    #initialize the game, and game resources.
    pygame.init()

    self.settings = Settings()

    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    #this controlls framerate as allowed by the CPU
    self.clock = pygame.time.Clock() 
  

  def run_game(self):
    #start the main loop for the game
    while True:
      #watch for keyboard and mouse events.
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
    #Redraw the screen during each pass through the loop.
      self.screen.fill(self.settings.bg_color)

      #Make the most recently drawn screen visible.
      pygame.display.flip()
      self.clock.tick(60)

if __name__ == '__main__':
  #Make a game instance, and run the game.
  ai = ElienInvasion()
  ai.run_game()