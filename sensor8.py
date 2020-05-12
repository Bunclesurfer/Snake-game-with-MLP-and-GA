# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:18:19 2020

@author: mwtod
"""


def direction_sensor(snake_start, apple_position, snake_position):
    distance_apple_1 = 0
    distance_snake_1 = 0
    distance_wall_1= 200
    distance_apple_2 = 0
    distance_snake_2 = 0
    distance_wall_2= 200
    distance_apple_3 = 0
    distance_snake_3 = 0
    distance_wall_3= 200
    distance_apple_4 = 0
    distance_snake_4 = 0
    distance_wall_4= 200
    distance_apple_5 = 0
    distance_snake_5 = 0
    distance_wall_5= 200
    distance_apple_6 = 0
    distance_snake_6 = 0
    distance_wall_6= 200
    distance_apple_7 = 0
    distance_snake_7 = 0
    distance_wall_7= 200
    distance_apple_8 = 0
    distance_snake_8 = 0
    distance_wall_8= 200
    
#direction_1
    for i in range(50):
        check_point = [ snake_start[0]+i*10 , snake_start[1] ]
        if check_point == apple_position:
            distance_apple_1 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0]+i*10 , snake_start[1] ]
        if check_point in snake_position[1:]:
            distance_snake_1 = 1/i
            break
    distance_wall_1 =  10/(501-snake_start[0])
    

#direction_2
    for i in range(50):
        check_point = [ snake_start[0]+i*10 , snake_start[1]+i*10 ]
        if check_point == apple_position:
            distance_apple_2 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0]+i*10 , snake_start[1]+i*10 ]
        if check_point in snake_position[1:]:
            distance_snake_2 = 1/i
            break
    distance_wall_2 = 10/min(501-snake_start[0], 501-snake_start[1])
    

#direction_3
    for i in range(50):
        check_point = [ snake_start[0] , snake_start[1]+i*10 ]
        if check_point == apple_position:
            distance_apple_3 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0] , snake_start[1]+i*10 ]
        if check_point in snake_position[1:]:
            distance_snake_3 = 1/i
            break
    distance_wall_3 = 10/(501-snake_start[1])
    

#direction_4
    for i in range(50):
        check_point = [ snake_start[0]-i*10 , snake_start[1]+i*10 ]
        if check_point == apple_position:
            distance_apple_4 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0]-i*10 , snake_start[1]+i*10 ]
        if check_point in snake_position[1:]:
            distance_snake_4 = 1/i
            break
    distance_wall_4 =  10/min(snake_start[0]+1, 501-snake_start[1])

    
#direction_5
    for i in range(50):
        check_point = [ snake_start[0]-i*10 , snake_start[1] ]
        if check_point == apple_position:
            distance_apple_5 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0]-i*10 , snake_start[1] ]
        if check_point in snake_position[1:]:
            distance_snake_5 = 1/i
            break
    distance_wall_5 =  10/(snake_start[0]+1)

    
#direction_6
    for i in range(50):
        check_point = [ snake_start[0]-i*10 , snake_start[1]-i*10 ]
        if check_point == apple_position:
            distance_apple_6 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0]-i*10 , snake_start[1]-i*10 ]
        if check_point in snake_position[1:]:
            distance_snake_6 = 1/i
            break
    distance_wall_6 =  10/(min(snake_start)+1)

    
#direction_7
    for i in range(50):
        check_point = [ snake_start[0] , snake_start[1]-i*10 ]
        if check_point == apple_position:
            distance_apple_7 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0] , snake_start[1]-i*10 ]
        if check_point in snake_position[1:]:
            distance_snake_7 = 1/i
            break
    distance_wall_7 =  10/(snake_start[1]+1)
  
    
#direction_8
    for i in range(50):
        check_point = [ snake_start[0]+i*10 , snake_start[1]-i*10 ]
        if check_point == apple_position:
            distance_apple_8 = 1
            break
    for i in range(50):
        check_point = [ snake_start[0]+i*10 , snake_start[1]-i*10 ]
        if check_point in snake_position[1:]:
            distance_snake_8 = 1/i
            break
    distance_wall_8 =   10/min(501-snake_start[0], snake_start[1]+1)
    
    return distance_apple_1,distance_snake_1,distance_wall_1,\
    distance_apple_2,distance_snake_2,distance_wall_2,\
    distance_apple_3,distance_snake_3,distance_wall_3,\
    distance_apple_4,distance_snake_4,distance_wall_4,\
    distance_apple_5,distance_snake_5,distance_wall_5,\
    distance_apple_6,distance_snake_6,distance_wall_6,\
    distance_apple_7,distance_snake_7,distance_wall_7,\
    distance_apple_8,distance_snake_8,distance_wall_8