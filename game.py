# Arden Boettcher
# 5/16/25
# Game Class

import pygame
import config
from board import Board


class Game():
  """This is where the actual gameplay is."""
  def __init__(self, screen, clock):
    self.screen = screen
    self.clock = clock

    self.balls = pygame.sprite.Group()
    self.powerups = pygame.sprite.Group()
    self.board = Board([20, 300])


  def run(self, running):
    self.running = running

    dt = 0

    while self.running:

      will_close = self.events()

      self.update(dt)

      self.draw()

      dt = self.clock.tick(config.FPS) / 1000

    return will_close


  def update(self, dt):
    self.board.update(dt)

    self.balls.update(dt)


  def draw(self):
    """Draws all of the game objects"""
    self.screen.fill(config.BLACK)

    self.board.draw(self.screen)

    pygame.display.flip()



  def events(self) -> bool:
    """Handles events for the game class"""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        return False

    return True