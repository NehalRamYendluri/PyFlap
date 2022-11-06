import pygame

class Display():
  def __init__(self,size,name):
    self.size = size
    self.name = name
    self.display = pygame.display.set_mode(size)
    pygame.display.set_caption(name)
  def update(self,player,keys,map):
    self.display.fill((255,255,255))
    map.draw(self)
    player.draw(self,keys)

    pygame.display.update()