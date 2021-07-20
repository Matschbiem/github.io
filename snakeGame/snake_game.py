import pygame
import time
import random

pygame.init()

disp_width = 600
disp_height = 400
disp = pygame.display.set_mode((disp_width,disp_height))
pygame.display.update()
pygame.display.set_caption("Snake game by Maxim")

bg = pygame.image.load("background_snake.PNG").convert()

blue = (50,153,213)
red = (213,50,80)
white = (255,255,255)
black = (0,0,0)
green = (0,255, 0)
yellow = (255,255,102)

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

def score (score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    disp.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        if x == 1:
            pygame.draw.rect(disp, black, [x[0], x[1], 30, 30])
        else:
            pygame.draw.rect(disp, black, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [25, disp_height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = disp_width/2
    y1 = disp_height/2  
    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            disp.fill(white)
            message("You Lost! Q-Quit or C-Play Again!", red)
            score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        disp.blit(bg, [0, 0])
        pygame.display.update()

        if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change

        pygame.draw.rect(disp, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        our_snake(snake_block, snake_list)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    
    pygame.quit()
    quit()


gameLoop()