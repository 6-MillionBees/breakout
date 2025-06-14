# Arden Boettcher
# 5/20/25
# Blocks class

import pygame
import config
from random import randint
from balls import Ball
from powerup import PowerUp

class Block(pygame.sprite.Sprite):
  """A simple Block"""
  def __init__(self, groups, pos):
    super().__init__(groups)
    self.health = 1
    self.rect = pygame.Rect(pos, (50, 25))
    self.color = config.WHITE

  def hit(self):
    pass

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)


class HardBlock(Block):
  """A Block that takes two hits"""
  def __init__(self, groups, pos):
    super().__init__(groups, pos)
    self.health = 2
    self.sprite = pygame.image.load("sprites/hardblock.png")
    pygame.transform.scale(self.sprite, (50, 25))
    self.rect = self.sprite.get_rect(topleft=pos)

  def hit(self):
    self.color = config.LIGHT_RED

  def draw(self, surface: pygame.Surface):
    pygame.draw.rect(surface, self.color, self.rect)
    surface.blit(self.sprite, self.rect)


class BallBlock(Block):
  def __init__(self, groups, pos, ball_group):
    super().__init__(groups, pos)
    self.ball_group = ball_group

  def draw(self, surface):
    pygame.draw.rect(surface, config.WHITE, self.rect)
    pygame.draw.circle(surface, config.BLACK, self.rect.center, 8)

  def kill(self):
    Ball(self.ball_group, self.rect.center, config.rand_vector(185, 355), config.WHITE, 7, 450)
    super().kill()



class PowerUpBlock(Block):
  def __init__(self, groups, pos, power_group):
    super().__init__(groups, pos)
    self.power_group = power_group
    self.sprite = pygame.Surface(self.rect.size)
    self.sprite.fill(config.WHITE)

    pygame.draw.rect(
      self.sprite,
      config.BLACK,
      pygame.Rect(
        config.sub_tup(config.sub_tup(self.rect.center, self.rect.topleft), (3, 8)), (6, 16))
    )

    pygame.draw.rect(
      self.sprite,
      config.BLACK,
      pygame.Rect(
        config.sub_tup(config.sub_tup(self.rect.center, self.rect.topleft), (8, 3)), (16, 6))
    )

  def draw(self, surface):
    surface.blit(self.sprite, self.rect)


  def kill(self):
    PowerUp(self.power_group, self.rect.center, "triple")
    super().kill()