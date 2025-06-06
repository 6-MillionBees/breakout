# Arden Boettcher
# 6/6/25
# powerups

import pygame
import config

class PowerUp(pygame.sprite.Sprite):
  def __init__(self, groups, pos: tuple, type: str) -> None:
    super().__init__(groups)
    self.pos = pos
    self.type = type
    self.rect = pygame.Rect((0, 0), (20, 20))
    self.rect.center = pos
    self.sprite = pygame.Surface(20, 20)
    pygame.draw.rect(self.sprite, config.GREEN, pygame.Rect((5, 0), (10, 20)))
    pygame.draw.rect(self.sprite, config.GREEN, pygame.Rect((0, 5), (20, 10)))


  def update(self, dt):
    self.move(dt)
    self.check_pos()


  def move(self, dt):
    self.pos = (self.pos[0], self.pos[1] + 20 * dt)
    self.rect.center = self.pos


  def check_pos(self):
    if self.pos >= config.HEIGHT + 20:
      self.kill()

  def draw(self, surface):
    surface.blit(self.sprite, self.rect)

