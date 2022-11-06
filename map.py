import random , pygame

class Map():
  def __init__(self,x_d,y_d,width,height):
    self.x_d = x_d
    self.y_d = y_d
    self.width = width
    self.surface = pygame.Surface((800,600))
    self.height1 = height
  def generate(self,screen):
    self.surface.fill((255,255,255))
    self.x = random.randint(300,400)
    self.y = 0
    self.height = random.randint(0,450) 
    pygame.draw.rect(self.surface,(0,0,0),(self.x,self.y,self.width,self.height))
    if self.height > screen.size[1]/2:
      self.height2 = self.height - self.y_d
      self.y2 = self.height - self.y_d
      print("h")
    else:
      self.height2 = screen.size[1] - (self.height + self.y_d) 
      self.y2 = self.height + self.y_d
    
    pygame.draw.rect(self.surface,(255,0,0),(self.x,self.y2,self.width,self.height1))  
    '''
    self.x += self.x_d
    self.y = 0
    self.height = random.randint(0,450) 
    pygame.draw.rect(self.surface,(0,0,0),(self.x,self.y,self.width,self.height))
    if self.height > screen.size[1]/2:
      self.height2 = self.height - self.y_d 
      self.y2 = self.height - self.y_d
      print("h")
    else:
      self.height2 = screen.size[1] - (self.height + self.y_d) 
      self.y2 = self.height + self.y_d
    
    pygame.draw.rect(self.surface,(255,0,0),(self.x,self.y2,self.width,self.height1))  
    '''
  def draw(self,screen):
    screen.display.blit(self.surface,(0,0))