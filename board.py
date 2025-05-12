# Arden Boettcher
# PLACEHOLDER
# Ship Class

import pygame as pg


class Board:
  def __init__(self, pos, color):
    self.pos = pos
    self.color = color
    self.destination = pg.mouse.get_pos()

  def update(self, dt):
    self.move(dt)
    self.check_pos()

  def move(self, dt):
    keys = pg.key.get_pressed()

  def draw(self, surface):
    pg.draw.rect(surface, self.color, pg.Rect(self.pos, (10, 10)))