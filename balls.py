# Arden Boettcher
# 5/16/25
# Balls

import pygame

class Ball(pygame.sprite.Sprite):
  def __init__(self,
      groups,
      pos: tuple,
      direction: pygame.math.Vector2,
      color: tuple,
      size = 10,
      speed = 100
    ) -> None:

    super().__init__(groups)
    self.pos = pos
    self.direction = direction
    self.color = color
    self.size = size


  def update(self, dt: int) -> None:
    """runs the Ball.move() and Ball.check_pos() methods"""
    self.move(dt)
    self.check_pos()


  def move(self, dt: int) -> None:
    self.pos += self.direction * 100 * dt



  def draw(self, surface: pygame.Surface) -> None:
    """Draws the Ball on a Surface using pygame.draw.circle()"""
    pygame.draw.circle(surface, self.color, self.pos, self.size)


  def colliderect(self, rect: pygame.Rect) -> bool:
    pass