# Arden Boettcher
# 5/16/25
# Balls

import pygame
import config

class Ball(pygame.sprite.Sprite):
  def __init__(self,
      groups,
      pos: tuple,
      direction: pygame.math.Vector2,
      color: tuple,
      radius = 10,
      speed = 100
    ) -> None:

    super().__init__(groups)
    self.pos = pos
    self.direction = direction
    self.color = color
    self.radius = radius


  def update(self, dt: int) -> None:
    """runs the Ball.move() and Ball.check_pos() methods"""
    self.move(dt)
    self.check_pos()


  def move(self, dt: int) -> None:
    self.pos += self.direction * 100 * dt


  def check_pos(self) -> list[int]:
    """This checks whether the ball is within the window and then returns a list of numbers 1: left, 2: right, 3: up, 4: down"""
    collisions = []
    if self.pos[0] - self.radius < 0:
      collisions.append(1)
    if self.pos[0] + self.radius > config.WIDTH:
      collisions.append(2)
    if self.pos[1] - self.radius < 0:
      collisions.append(3)
    if self.pos[1] + self.radius > config.HEIGHT:
      collisions.append(4)

    return collisions


  def draw(self, surface: pygame.Surface) -> None:
    """Draws the Ball on a Surface using pygame.draw.circle()"""
    pygame.draw.circle(surface, self.color, self.pos, self.radius)


  def colliderect(self, rect: pygame.Rect) -> bool:
    dist_x = abs(self.pos[0] - rect.x)
    dist_y = abs(self.pos[1] - rect.y)

    if dist_x > (rect.width / 2 + self.radius): return False
    if dist_y > (rect.height / 2 + self.radius): return False

    if dist_x <= (rect.width / 2): return True
    if dist_y <= (rect.height / 2): return True

    corner_dist = (dist_x - rect.width / 2) ** 2 + (dist_y - rect.height / 2) ** 2

    return corner_dist <= self.radius ** 2