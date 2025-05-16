# Arden Boettcher
# Insert date here
# Insert title here

import pygame
from random import randint
from math import radians, cos, sin

# Screen size constants
WIDTH = 500
HEIGHT = 500

# Framerate
FPS = 60

# Color Constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




# Outline

def outline(rect, weight = 2):
  outrect = pygame.Rect(rect.x - weight, rect.y - weight, rect.width + weight * 2, rect.height + weight * 2)
  # pygame.draw.rect(surface, color, outrect)
  return outrect


# Rainbow

def rainbow(color: list[int], step = 1):
  hsva = pygame.color.Color(color)
  try:
    hsva.hsva = (hsva.hsva[0] + step, hsva.hsva[1], hsva.hsva[2], hsva.hsva[3])
  except ValueError:
    hsva.hsva = (hsva.hsva[0] - 360 + step, hsva.hsva[1], hsva.hsva[2], hsva.hsva[3])
  rgb = (hsva.r,  hsva.g, hsva.b)
  return rgb


# Random Vector

def rand_vector(min_angle = 0, max_angle = 360):
  angle = radians(randint(min_angle, max_angle))
  x = cos(angle)
  y = sin(angle)
  return pygame.math.Vector2(x, y)


# Draw Text

class Text():
  """A simple Text() class that helps with centering, drawing, and storing data"""
  def __init__(self, words: str, font: pygame.font.Font, color: tuple, pos: tuple, antialias = False):
    self.text = font.render(words, antialias, color)
    self.color = color
    self.rect = self.text.get_rect(topleft=pos)

  def center(self, center):
    self.rect.center = center
    return self

  def draw(self, surface: pygame.Surface):
    surface.blit(self.text, self.rect)