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
      speed = 500
    ) -> None:

    super().__init__(groups)
    self.pos = pos
    self.direction = direction
    self.color = color
    self.radius = radius
    self.speed = speed


  def update(self, dt: int) -> None:
    """runs the Ball.move() and Ball.check_pos() methods"""
    self.move(dt)

    for bounce in self.check_pos():
      if bounce == 1:
        self.direction.reflect_ip(pygame.math.Vector2(1, 0))
      elif bounce == 2:
        self.direction.reflect_ip(pygame.math.Vector2(0, 1))


  def move(self, dt: int) -> None:
    # self.pos = pygame.mouse.get_pos()
    self.pos += self.direction * self.speed * dt


  def check_pos(self) -> list[int]:
    """This checks whether the ball is within the window and then returns a list of numbers 1: left, 2: right, 3: up, 4: down"""
    collisions = []
    if self.pos[0] - self.radius < 0:
      self.pos[0] = 0 + self.radius
      collisions.append(1)
    elif self.pos[0] + self.radius > config.WIDTH:
      self.pos[0] = config.WIDTH - self.radius
      collisions.append(1)
    if self.pos[1] - self.radius < 0:
      self.pos[1] = 0 + self.radius
      collisions.append(2)
    elif self.pos[1] + self.radius > config.HEIGHT + 10:
      self.kill()

    return collisions


  def draw(self, surface: pygame.Surface) -> None:
    """Draws the Ball on a Surface using pygame.draw.circle()"""
    pygame.draw.circle(surface, self.color, self.pos, self.radius)


  def colliderect(self, rect: pygame.Rect) -> int:
    """checks if """

    dist_x = abs(self.pos[0] - rect.center[0])
    dist_y = abs(self.pos[1] - rect.center[1])

    if dist_x > (rect.width / 2 + self.radius): return 0
    if dist_y > (rect.height / 2 + self.radius): return 0

    if dist_x <= (rect.width / 2): return 1
    if dist_y <= (rect.height / 2): return 2

    if (dist_x - rect.width / 2) ** 2 + (dist_y - rect.height / 2) ** 2 <= self.radius ** 2:
      return 3

    return 0