import pygame

class Player():
  def __init__(self,x,y,height,width,color):
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.color = color
    self.y_vel = 0
    self.x_vel =0
    self.acc = 0.05
  def move(self,screen,keys):
    self.y_vel += self.acc
    self.y += self.y_vel
    if keys[pygame.K_SPACE]: 
      self.y_vel = -3
    if self.y > screen.size[1]-self.height:
      self.y = 0
      self.y_vel = 0
  def draw(self,screen,keys):
    self.move(screen,keys)
    self.player = pygame.Surface((self.width,self.height))
    screen.display.blit(self.player,(self.x,self.y))

    