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
game_over= False

x1 = 150
y1 = 150

x1_change = 0
y1_change = 0

clock = pygame.time.Clock() 


while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over== True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0 
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

    x1 += x1_change
    y1 += y1_change
    dis.fill(green)
    pygame.draw.rect(dis, purple,[x1, y1, 10, 10])


    pygame.display.update()

    clock.tick(15)

pygame.quit()
quit()


