# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:15:50 2020

@author: hippo 
"""



from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import random



def generate_model(population):
    """
    

    Parameters
    ----------
    population : INT
        how many model(population) would you create

    Returns
    -------
    pop : LIST
        List of keras sequential model (MLP)

    """
    
    pop =[]
    for _ in range(population):
        model = Sequential()
        model.add(Dense(units=16, input_dim=24, kernel_initializer='normal', activation='relu',bias_initializer='normal'))
        model.add(Dense(units=16, kernel_initializer='normal', activation='relu',bias_initializer='normal'))
        model.add(Dense(units=4, kernel_initializer='normal', activation='softmax'))
        pop.append(model)

    return pop


def crossover(mom, dad, son_population):
    """
    

    Parameters
    ----------
    mom : keras sequential model
        
    dad : keras sequential model
        
    son_population : INT
        how many son would you create

    Returns
    -------
    son : LIST
        List of keras sequential model

    """
    mom_weight = mom.get_weights()
    dad_weight = dad.get_weights()
    son = generate_model(son_population)
    
    for count in range(son_population):        
        son_weight = mom.get_weights()
        for i in range(len(mom_weight)):
            for j in range(len(mom_weight[i])):
                if mom_weight[i][j].ndim > 0:
                    for k in range(len(mom_weight[i][j])):
                        son_weight[i][j, k] = random.choice([dad_weight[i][j, k], mom_weight[i][j, k]])
                else:
                    son_weight[i][j] = random.choice([dad_weight[i][j], mom_weight[i][j]])
            
        son[count].set_weights(son_weight)
    
    return son


def mutate(model, mutate_rate = 0.1):
    """
    

    Parameters
    ----------
    model : keras sequential model
        DESCRIPTION.
    mutate_rate : chance of mutate
        DESCRIPTION. The default is 0.1.

    Returns
    -------
    None.

    """
    weight = model.get_weights()
    
    for i in range(len(weight)):
        for j in range(len(weight[i])):
            if weight[i][j].ndim > 0:
                for k in range(len(weight[i][j])):
                    if random.random() < mutate_rate:                        
                        weight[i][j, k] = weight[i][j, k] + random.gauss(0,0.4)
            else:
                if random.random() < mutate_rate:                        
                        weight[i][j] = weight[i][j] + random.gauss(0,0.4)
    
    weight[len(weight)-1][:3] = 0
    model.set_weights(weight)
    #return model




def get_next_gen(this_gen, this_gen_fittness, best_model, gen_score, gen_index, max_score, mutate_pop_rate):
    
    sorted_index = sorted(range(len(this_gen_fittness)), key = lambda k : this_gen_fittness[k], reverse=True) 
    sorted_gen = []
    for i in range(20):
        sorted_gen.append(this_gen[sorted_index[i]])
    
    best_model.append(sorted_gen[0].get_weights())
    
    #crossover no1 no2
    son = crossover(sorted_gen[0], sorted_gen[1], 60)    
    for i in range(len(son)):
        sorted_gen.append(son[i])
    
    #crossover no1 no3
    son = crossover(sorted_gen[0], sorted_gen[2], 50)    
    for i in range(len(son)):
        sorted_gen.append(son[i])
    
    #crossover no2 no3
    son = crossover(sorted_gen[1], sorted_gen[2], 40)    
    for i in range(len(son)):
        sorted_gen.append(son[i])    
    
    #crossover no2 no4
    son = crossover(sorted_gen[1], sorted_gen[3], 30)    
    for i in range(len(son)):
        sorted_gen.append(son[i])
    
    
    for i in range(len(sorted_gen)):
        if i > 4:
            if random.random() < mutate_pop_rate:
                mutate(sorted_gen[i])
    
    
    gen_score.append(max_score)
    gen_index += 1
    
    print('Gen ', (gen_index), ' created')            
    return sorted_gen, best_model, gen_index

