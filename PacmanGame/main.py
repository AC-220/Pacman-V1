import pygame
from pacman import Pacman  # importing classes from different game aspects into main file 
from enemy import Enemy
from food2 import Food

# initialise pygame
pygame.init()
# ---SETUP---
# setup characteristics of the drawable components
display_width = 500
display_height = 500
display_size = [display_width, display_height]

# creating display window
display = pygame.display.set_mode(display_size) # parameter must be list or tuple

# characteristics of the object

# characteristics of pacman 
circle_x = 100  # x-coordinate of circle
circle_y = 50 # y-coordinate of circle
circle_coordinates = [circle_x, circle_y]
circle_radius = 10
circle_colour = [255, 0, 255]

pacman = Pacman(circle_x, circle_y, circle_radius, circle_colour, 2) # creating an instance of the class Pacman
enemy = Enemy(150, 100, [0, 0, 255], 2, 2) # creating an instance of the class Enemy

dark_grey = [50, 50, 50] # colour of background

#setting up food 
food_x = circle_x - circle_radius # x-coordinate of food
food_y = display_height // 2 # y-coordinate of food
food_1 = Food(food_x, food_y) # creating an instance of the class Food

# initialise Clock (amount of times per second the screen refreshes)
clock = pygame.time.Clock() 

# ---Game Loop--- 
# run_game = True
run_game = True
isMovingDown = False # different booleans to check make pacman move 
isMovingUp = False
isMovingLeft = False    
isMovingRight = False

while run_game: 
# ------ draw display window
    display.fill(dark_grey) # colour passes in here for background of screen 
    
# ------ prepare drawable elements
    pacman.draw(display)
    enemy.draw(display)
    food_1.draw(display)
#    pygame.draw.circle(display, circle_colour, [circle_x, circle_y], circle_radius)
#    circle_y = circle_y + 1
#     print(circle_y)
#     print(circle_coordinates)

# ------ listen to events and respond:
    for event in pygame.event.get(): # loops though pygame events 
# ------ listen out to mouse, keyboard etc events and when application is quit
        if event.type == pygame.QUIT:  # if event is quit
            run_game = False # exits game loop
            
        elif event.type == pygame.KEYDOWN: # if user presses down on a key 
            if event.key == pygame.K_DOWN: # if the key they press is down arrow 
                isMovingDown = True     # pacman is moving down 
            if event.key == pygame.K_UP: # if the key they press is up arrow 
                isMovingUp = True     # pacman is moving up 
            if event.key == pygame.K_LEFT and (event.key != pygame.K_DOWN or event.key != pygame.K_UP): # ensures that when left key is pressed down and up are not also pressed to avoid moving diagonally
                isMovingLeft = True # pacman moves left
            if event.key == pygame.K_RIGHT:
                isMovingRight = True  
                  
        elif event.type == pygame.KEYUP: # if user releases press on the key 
            if event.key == pygame.K_DOWN: # pacman stops moving in these directions 
                isMovingDown = False
            if event.key == pygame.K_UP:
                isMovingUp = False
            if event.key == pygame.K_LEFT:
                isMovingLeft = False
            if event.key == pygame.K_RIGHT:
                isMovingRight = False
                
        if event.type == pygame.KEYDOWN: # if space is pressed then relocate food method is called to relocate food to random location
            if event.key == pygame.K_SPACE: 
                food_1.relocate(display_height)        
    
     
    if isMovingDown:  # when isMovingDown variable is true 
        pacman.move_down(display_size[1]) # calls move_down method and passes y value making pacman moves down the y axis at the speed defined within the method
        
    elif isMovingUp:
        pacman.move_up(display_size[1]) # calls move_up function and passes y value to make it move up the y axis 
        
    elif isMovingLeft:
        pacman.move_left(display_size[0]) # calls move_left method so pacman moves along the x axis to the left 
        
    elif isMovingRight:
        pacman.move_right(display_size[0]) # calls move right method 
        
        
    # Check for collision between pacman and food     
    food_centre = food_1.get_size()[1] // 2 # finds centre point of the food item 
    distance = ((pacman.get_x() - food_1.get_x())** 2 + (pacman.get_y() - food_1.get_y())** 2)** 0.5 # calculates the euclidean distance between pacman and the food 
    collision = circle_radius + food_centre # this is the collision threshold to test if they have collided
    if distance < collision: # tests if distance is less than the collision threshold , means they have collided 
        food_1.relocate(display_height, display_width)   # relocates all objects to random locations and passing in the display windows dimensions as a limit for the relocation 
        #pacman.relocate(display_height, display_width)
        enemy.relocate(display_height, display_width)
    
    #Check for collision between enemy and food
    enemy_distance = ((enemy.get_x() - food_1.get_x())** 2 + (enemy.get_y() - food_1.get_y())** 2)** 0.5 # this is the euclidean distance between enemy and food
    if enemy_distance < collision: #tests collision threshold with the enemys distance 
        food_1.relocate(display_height, display_width) #then resets game and objects aswell 
        #enemy.relocate(display_height, display_width)
        pacman.relocate(display_height, display_width)
        
    # check for collision between pacman and the enemy
    pacEnemy_distance = ((pacman.get_x() - enemy.get_x())** 2 + (pacman.get_y() - enemy.get_y())** 2)** 0.5 # distance betwen pacman and enemy
    collision2 = circle_radius + enemy.get_radius() # new collision threshold for enemy and pacman 
    if pacEnemy_distance < collision2:
        pacman.relocate(display_height, display_width)
        enemy.relocate(display_height, display_width)
    
    
    
    # enemy chase food
    if abs(food_1.get_y() - enemy.get_y()) > abs(food_1.get_x() - enemy.get_x()): # this if statement uses the absolute value of the y value difference between the food and the enemy and compares it to the absolute value of the x value difference between food and enemy 
        if food_1.get_y() > enemy.get_y() - food_centre:    # if the food is lower than the enemy than the enemy is moved down 
            enemy.move("DOWN", display_width,display_height)
        elif food_1.get_y() < enemy.get_y() + food_centre: # if the food is higher than the enemy than "UP" is passed into move to move enemy up
            enemy.move("UP", display_width,display_height)
    else:
        if food_1.get_x() > enemy.get_x() - food_centre: # if the food x value is further left on the x axis than the enemy is passed to move right 
            enemy.move("RIGHT",display_width,display_height)
        elif food_1.get_x() < enemy.get_x() + food_centre: # if the food x value is lower, further right, than the enemy moves left chasing the food  
            enemy.move("LEFT",  display_width,display_height)

        
# ------ if application is quit --> run_game = False (break out of game loop)
# ------ update display window (prepared drawable elements will not appear without this)
    pygame.display.update()     
# ------ update the Clock (framerate)
    clock.tick(60)

# when game loop terminates
# deinitialise pygame
pygame.quit()
# quit application
quit()