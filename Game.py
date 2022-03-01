import pygame, sys,random

# #Tạo background cho game
# bg = pygame.image.load('picture/chi.jpg').convert()
# bg = pygame.transform.scale2x(bg)
# bg = pygame.image.load('picture/')

pygame.init()  #start game
screen  = pygame.display.set_mode((432,768)) #set size picure douple picure

#tạo vòng lặp
while True:
     for event in pygame.event.get(): #Get event in game
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update() #display up monitor
          
     


