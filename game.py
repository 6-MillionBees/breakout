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
    self.board = Board([20, 400])
    self.blocks = []
    self.make_blocks()


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

    for ball in self.balls.sprites():
      ball: Ball
      if ball.colliderect(self.board.rect):
        ball.direction = pygame.math.Vector2(
          config.sub_tup(ball.pos, self.board.rect.center)
          ).normalize()

    if not self.blocks:
      self.make_blocks()


  def draw(self):
    """Draws all of the game objects"""
    self.screen.fill(config.BLACK)

    self.board.draw(self.screen)

    for ball in self.balls.sprites():
      ball.draw(self.screen)

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
        choice = randint(1, 10)
        if choice < 5:
          blocks.Block(self.blocks, block_pos)
        elif choice == 6:
          blocks.HardBlock(self.blocks, block_pos)