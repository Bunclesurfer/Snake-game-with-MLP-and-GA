# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:13:57 2020

@author: mwtod
"""


import pygame
import random
import numpy as np

snake_color  = (62, 49, 41)
apple_color = (255, 0, 0)
ground_color = (247, 255, 224)
info_color = (255,238,226)
text_color = (74, 76, 78)



def display_snake(snake_position, display):
    for position in snake_position:
        pygame.draw.rect(display, snake_color, pygame.Rect(position[0], position[1], 10, 10))


def display_apple(apple_position, display):
    pygame.draw.rect(display, apple_color, pygame.Rect(apple_position[0], apple_position[1], 10, 10))


def starting_positions():
    snake_start = [100, 100]
    snake_position = [[100, 100], [90, 100], [80, 100]]
    apple_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
    score = 0

    return snake_start, snake_position, apple_position, score



def generate_snake(next_position, snake_position, apple_position, button_direction, score, stepLeft):
    

    if next_position == apple_position:
        apple_position, score = collision_with_apple(apple_position, score)
        snake_position.insert(0, list(next_position))
        stepLeft = min(stepLeft+100, 500)
        
    else:
        snake_position.insert(0, list(next_position))
        snake_position.pop()

    return snake_position, apple_position, score, stepLeft


def collision_with_apple(apple_position, score):
    apple_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
    score += 1
    return apple_position, score


def collision_with_boundaries(snake_start):
    if snake_start[0] >= 500 or snake_start[0] < 0 or snake_start[1] >= 500 or snake_start[1] < 0:
        return 1
    else:
        return 0


def collision_with_self(snake_start, snake_position):
    if snake_start in snake_position:
        return 1
    else:
        return 0



def generate_next_position(snake_start,button_direction,prev_direction):
    if button_direction == 0 and prev_direction == 1:
        button_direction = 1  
    elif button_direction == 1 and prev_direction == 0:
        button_direction = 0
    elif button_direction == 2 and prev_direction == 3:
        button_direction = 3
    elif button_direction == 3 and prev_direction == 2:
        button_direction = 2

    
    if button_direction == 0 :
        next_position =[snake_start[0]-10 ,snake_start[1]]
    if button_direction == 1 :
        next_position =[snake_start[0]+10 ,snake_start[1]]
    if button_direction == 2 :
        next_position =[snake_start[0] ,snake_start[1]+10]
    if button_direction == 3 :
        next_position =[snake_start[0] ,snake_start[1]-10]
    
    return next_position, button_direction





def play_game(next_position, snake_position, apple_position, button_direction, score, display, clock, alive, stepLeft):
    
    crashed = False
    while crashed is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        
     
        snake_position, apple_position, score, stepLeft = generate_snake(next_position, snake_position, apple_position,\
                                                               button_direction, score, stepLeft)

        
        display.fill(ground_color, pygame.Rect(0, 0, 500, 500))
        display.fill(info_color, pygame.Rect(500, 0, 300, 500))
        display_apple(apple_position, display)
        display_snake(snake_position, display)
                
        
        pygame.display.set_caption("SCORE: " + str(score))
        #pygame.display.update()
        clock.tick(30)

        return snake_position, apple_position, score, stepLeft