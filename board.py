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
    self.speed = [500, 500]
    self.rect = pygame.Rect(self.pos, (100, 10))

  def update(self, dt):
    """Runs the Board.move() and the Board.check_pos() methods"""
    self.move(dt)
    self.check_pos()
    self.rect = pygame.Rect(self.pos, (100, 10))

  def move(self, dt):
    """Checks input and moves depending on which keys are pressed"""
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
      self.pos[0] += self.speed[0] * dt
    if keys[pygame.K_LEFT]:
      self.pos[0] -= self.speed[1] * dt

  def check_pos(self):
    if self.pos[0] < 0:
      self.pos[0] = 0
    elif self.pos[0] + self.rect.width > config.WIDTH - 1:
      self.pos[0] = config.WIDTH - self.rect.width


  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)