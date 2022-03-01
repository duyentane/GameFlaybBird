import pygame, sys,random

pygame.init()  #start game
screen  = pygame.display.set_mode((432,768)) #set size picure douple picure

#Create time quickly or slowly
clock =  pygame.time.Clock()

#Create background for game
bg = pygame.image.load('picture/chi.jpg').convert()
bg = pygame.transform.scale2x(bg)
floor = pygame.image.load('picture/floor.png').convert()
floor = pygame.transform.scale2x(floor)

#Create loop game
while True:
     for event in pygame.event.get(): #Get event in game
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     screen.blit(bg,(0,0))
     screen.blit(floor,(0,600))
     pygame.display.update() #display up monitor
     clock.tick(120)
          
     


