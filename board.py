# Arden Boettcher
# PLACEHOLDER
# Ship Class

import pygame
import config


class Board:
  """A rectangle, it can move left and right"""
  def __init__(self, pos, color = config.WHITE):
    self.pos = pos
    self.color = color
    self.destination = pygame.mouse.get_pos()
    self.speed = [75, 75]

  def update(self, dt):
    """Runs the Board.move() and the Board.check_pos() methods"""
    self.move(dt)
    self.check_pos()

  def move(self, dt):
    """Checks input and moves depending on which keys are pressed"""
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
      self.pos += self.speed[0] * dt
    if keys[pygame.K_LEFT]:
      self.pos -= self.speed[1] * dt

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, pygame.Rect(self.pos, (10, 10)))