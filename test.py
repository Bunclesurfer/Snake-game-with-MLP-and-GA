# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:17:50 2020

@author: hippo
"""


import tensorflow as tf
from sensor8 import * 
import numpy as np
from GA_func import *
from tqdm import tqdm, trange
from game import *


def run_game_with_ML(model, display, clock, pop_no, gen_index):
    max_score = 0
    total_score = 0
    total_result = 0
    test_games = 10

    for game_count in range(test_games):
        snake_start, snake_position, apple_position, score = starting_positions()
        
        prev_direction = 1
        alive = 0
        stepLeft = 200
        
        
        while stepLeft > 0:
            #catch 8 direction, 24 input,and reshape 
            snake_start = snake_position[0]
            sensor_feedback = np.array(direction_sensor(snake_start, apple_position, snake_position)).reshape(1,24).astype('float32')
            #use model.predict to get next direction
            button_direction = model.predict_classes(sensor_feedback)[0]
            
            #get next snake_head position
            next_position, button_direction = generate_next_position(snake_start,button_direction,prev_direction)
            
            #whether the snake will collision with wall or itself
            if collision_with_boundaries(next_position) == 1 or collision_with_self(next_position ,snake_position) == 1:
                break

            
            
            
            snake_position, apple_position, score, stepLeft = play_game(next_position, snake_position, apple_position,
                                                              button_direction, score, display, clock, alive, stepLeft)
            
            
            #infomation to be displayed 
            info_stepLeft  = "Step Left: " + str(stepLeft)
            info_max_score = "Max Score: " + str(max_score)
            info_game_count= "Game Tested: " + str(game_count)
            info_gen_count = "Generation: " + str(gen_index)
            info_pop_count= "Snake no. " + str(pop_no)
            #info_apple    = str(sensor_feedback[0,0:22:3])
            info_font = pygame.font.SysFont("arial", 24)

            display.blit(info_font.render(info_gen_count, True, text_color), (510, 30))
            display.blit(info_font.render(info_pop_count, True, text_color), (510, 50))
            display.blit(info_font.render(info_game_count, True, text_color), (510, 70))
            display.blit(info_font.render(info_max_score, True, text_color), (510, 90))
            display.blit(info_font.render(info_stepLeft, True, text_color), (510, 110))
            #display.blit(info_font.render(info_apple, True, text_color), (510, 130))
            
            pygame.display.update()
            prev_direction = button_direction
            result = score + alive/100
            alive += 1
            stepLeft -= 1
            if score > max_score:
                max_score = score

        total_score += score
        total_result += result
        progress.update(1)

    return total_result/10, max_score, total_score/10

def test_generation(model, gen_index, population, display, clock):
    model_fittness = []
    model_max = 0
    
    for i in range(population):
        avg_result ,max_score, avg_score = run_game_with_ML(model[i],display,clock, i, gen_index)
        model_fittness.append(avg_result)
        if max_score > model_max:
            model_max = max_score
            
    return model_fittness, model_max
            



pygame.init()
display=pygame.display.set_mode((800,500))
clock=pygame.time.Clock()



gen_index = 540
#best model of each generation
best_model = []
# max apple eated of each generation
gen_score = []
# max fitness of each generation
gen_fitness = []
# choose how many population will mutate
mutate_pop_rate = 0.1
max_score = 0
population = 200



 

#load weight to model
this_gen = generate_model(population)
for i in range(population):
    this_gen[i].set_weights(this_gen_weight[i])
    


# save weight
this_gen_weight = []
for i in range(population):
    this_gen_weight.append(this_gen[i].get_weights())


# total = population * game per snake * how many generation
progress = tqdm(total=160000)
for _ in range(80):
    this_gen_fittness, max_score = test_generation(this_gen, gen_index, population, display, clock)
    print("\nMax score of generation: ", gen_index, ': ', max_score)
    print("Fittness of generation: ", gen_index, ' :', max(this_gen_fittness))
    gen_fitness.append(max(this_gen_fittness))
    this_gen, best_model, gen_index = get_next_gen(this_gen, this_gen_fittness, best_model, gen_score, gen_index, max_score, mutate_pop_rate)    
progress.close()    



