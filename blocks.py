# Arden Boettcher
# 5/20/25
# Blocks class

import pygame
import config
from random import randint

class Block(pygame.sprite.Sprite):
  """A simple Block"""
  def __init__(self, groups, pos):
    super().__init__(groups)
    self.health = 1
    self.rect = pygame.Rect(pos, (50, 25))
    self.color = config.WHITE

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)


class HardBlock(Block):
  """A Block that takes two hits"""
  def __init__(self, groups, pos):
    super().__init__(groups, pos)
    self.health = 2
    self.sprite = pygame.image.load()