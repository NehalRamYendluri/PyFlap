import pygame ,sys
from display import Display
from player import Player
from map import Map
size = (800,500)
name = "project"
screen = Display(size,name)
player = Player(100,100,20,20,((0,0,0)))
map = Map(200,100,20,400)
map.generate(screen)
FPS = 60
while True:
  pygame.time.Clock().tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  keys = pygame.key.get_pressed()
  screen.update(player,keys,map)