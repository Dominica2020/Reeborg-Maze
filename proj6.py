def turn_right():
    turn_left()
    turn_left()
    turn_left()  
    
while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
     else:
        turn_left()    
    
# Advanced Debug    
    
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
