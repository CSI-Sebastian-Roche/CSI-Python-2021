import pygame
import time 
pygame.init()

purple = (151,70, 250) #snake
orange = (240, 100, 65) #game over
yellow= (245, 243, 81) #food
green= (65, 224, 120) #bacground color
blue= (75, 107, 250) #score

dis_width = 400
dis_height = 300

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("The Snake game")
game_over= False




clock = pygame.time.Clock() 
snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(mg, True, color)
    dis.blit(mesg, [dis_width/7, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0


while not game_over:

    while game_close == True:
        dis.fill(green)
        message("You took the L Q-Quit or P-Play Again", orange)

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                for event in pygame.event.get():
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_q:
                        gameLoop()


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over== True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0 
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True 

    x1 += x1_change
    y1 += y1_change
    dis.fill(green)
    pygame.draw.rect(dis, purple,[x1, y1, snake_block, snake_block])


    pygame.display.update()

    clock.tick(snake_speed)


pygame.quit()
quit()


