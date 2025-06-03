# Arden Boettcher
# Insert date here
# Insert title here

import sys
import pygame
import config
from game import Game

class Main:
  """Main() is just a glorified menu that opens when you run the game"""
  def __init__(self):
    pygame.init()
    pygame.mixer.init()

    # Window
    self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("PLACEHOLDER")

    # Clock
    self.clock = pygame.time.Clock()

  def run(self):
    # The bool for the main loop
    self.running = True

    self.start_button = pygame.Rect((0, 0), (200, 75))
    self.start_button.center = (config.WIDTH / 2, config.HEIGHT / 2 + 75)

    self.prev_score = 0

    self.score_text = config.Text(str(self.prev_score), config.mainfont, config.WHITE, (0, 0))
    self.score_text.center((config.WIDTH / 2, 200))

    dt = 0
    # Main loop
    while self.running:

      # Call events / update running
      self.main_events()


      # Fills window
      self.screen.fill(config.BLACK)

      pygame.draw.rect(self.screen, config.WHITE, self.start_button)

      self.score_text.draw(self.screen)

      # Updates the Display
      pygame.display.flip()

      # Limits the framerate
      dt = self.clock.tick(config.FPS) / 1000


  # Event Handling
  def main_events(self):
    for event in pygame.event.get():

      # Quits the game when you press the x
      if event.type == pygame.QUIT:
        self.running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.start_button.collidepoint(event.pos):

          # This runs the actual game
          self.prev_score = Game(self.screen, self.clock).run(self.running)
          self.score_text.set_text(str(self.prev_score), config.WHITE)
          self.score_text.center((config.WIDTH / 2, 200))


  # Exits the code
  def quit(self):
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
  # This is the only code that actually "runs"
  main = Main()
  main.run()
  # Closes the game for good
  main.quit()
