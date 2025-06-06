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

# Fonts
pygame.font.init()
mainfont = pygame.font.Font("highway-encounter.ttf", 20)

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
LIGHT_RED = (255, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Events

MAKEPOWERUP = pygame.event.custom_type()

class MakePowerup:
  def __init__(self, power, pos):
    self.type = MAKEPOWERUP
    self.pos = pos
    self.power = power



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


# Coordiate Math
def add_tup(tuple1, tuple2):
  """Adds the first number of tuple1 to the first number of tuple2 and so on"""
  temp_list = []
  for x in range(len(tuple1)):
    temp_list.append(tuple1[x] + tuple2[x])

  return tuple(temp_list)

def sub_tup(tuple1, tuple2):
  """Subtracts the first number of tuple1 to the first number of tuple2 and so on"""
  temp_list = []
  for x in range(len(tuple1)):
    temp_list.append(tuple1[x] - tuple2[x])

  return tuple(temp_list)



# Text Class
class Text():
  """A simple Text() class that helps with centering, drawing, and storing data"""
  def __init__(self, words: str, font: pygame.font.Font, color: tuple, pos: tuple, antialias = False):
    self.text = font.render(words, antialias, color)
    self.font = font
    self.color = color
    self.rect = self.text.get_rect(topleft=pos)

  def center(self, center: tuple):
    self.rect.center = center
    return self

  def set_text(self, text: str, color, antialias = False, background = None):
    self.text = self.font.render(text, antialias, color, background)
    self.rect = self.text.get_rect()
    return self

  def draw(self, surface: pygame.Surface):
    surface.blit(self.text, self.rect)