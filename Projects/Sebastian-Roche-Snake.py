import pygame
pygame.init()

purple = (151,70, 250) #snake
orange = (240, 100, 65) #game over
yellow= (245, 243, 81) #food
green= (65, 224, 120) #bacground color
blue= (75, 107, 250) #score

dis=pygame.display.set_mode((400,300))
pygame.display.upset()
pygame.display.set_caption("The Snake game")
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over== True 
pygame.quit()
quit()


