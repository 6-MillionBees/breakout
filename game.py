# Arden Boettcher
# 5/16/25
# Game Class

import pygame
import config
import blocks
from random import randint
from board import Board
from balls import Ball


class Game():
  """This is where the actual gameplay is."""
  def __init__(self, screen, clock):
    self.screen = screen
    self.clock = clock

    self.balls = pygame.sprite.Group()
    self.powerups = pygame.sprite.Group()
    self.blocks = pygame.sprite.Group()
    self.board = Board([200, 400])
    Ball(self.balls, (250, 250), pygame.math.Vector2(0, -1), config.RED)
    self.make_blocks()


  def run(self, running):
    self.running = running
    self.points = 0


    dt = 0

    while self.running:

      will_close = self.events()

      self.update(dt)

      self.draw()

      dt = self.clock.tick(config.FPS) / 1000

      if not self.balls.sprites():
        self.running = False

    return will_close


  def update(self, dt):
    self.board.update(dt)

    self.balls.update(dt)

    for ball in self.balls.sprites():
      ball: Ball
      collision = ball.colliderect(self.board.rect)
      if collision:
        ball.direction = pygame.math.Vector2(
          config.sub_tup(ball.pos, config.add_tup(self.board.rect.center, [0, 10]))
          ).normalize()
        if ball.direction.y > 0:
          ball.direction.y *= -1


    for ball in self.balls.sprites():
      ball: Ball
      for block in self.blocks.sprites():
        block: blocks.Block
        collision = ball.colliderect(block.rect)
        if collision:
          if collision == 1:
            ball.direction.reflect_ip(pygame.math.Vector2(1, 0))
          elif collision == 2:
            ball.direction.reflect_ip(pygame.math.Vector2(0, 1))
          elif collision == 3:
            ball.direction = pygame.math.Vector2(
              config.sub_tup(
                ball.pos,
                block.rect.center
                )
              ).normalize()
          block.health -= 1
          if block.health <= 0:
            block.kill()
            self.points += 1

    if not self.blocks:
      self.make_blocks()


  def draw(self):
    """Draws all of the game objects"""
    self.screen.fill(config.BLACK)

    self.board.draw(self.screen)

    for ball in self.balls.sprites():
      ball.draw(self.screen)

    for block in self.blocks.sprites():
      block.draw(self.screen)

    pygame.display.flip()


  def events(self) -> bool:
    """Handles events for the game class"""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        return False

    return True



  def make_blocks(self):
    for x in range(8):
      for y in range(3):
        block_pos = (x * 55 + 50, y * 30 + 50)
        blocks.HardBlock(self.blocks, block_pos)