import pygame 
import random
 
class Enemy:

    def __init__(self, x, y, colour, speed_x, speed_y):
        self.__x = x
        self.__y = y
        self.__radius = 10
        self.__colour = colour
        self.__speed_x, self.__speed_y = speed_x, speed_y # this defines the speed of the enemy in different axis

    def draw(self, display):
        pygame.draw.circle(display, self.__colour, [self.__x, self.__y], self.__radius) # circle is draw as the enemy 

    def move(self,direction,display_width=None,display_height=None): # when move is called it takes the direction parameter and is then check in if statements below to determine the direction enemy moves 
        
        if direction == "UP":
            if self.__y > self.__radius: # moves enemy upwards along y axis as long as within borders 
                self.__y -= self.__speed_y
        elif direction == "DOWN":
            self.__y += self.__speed_y # increases y coordinate to move enemy down 
            if self.__y > display_height - self.__radius: # ensures enemy is not past into the border and off the screen 
                self.__y = display_height - self.__radius
        elif direction == "RIGHT":
            self.__x += self.__speed_x      # increases x value to move enemy along to the right at the speed defined in the method calling 
            if self.__x > display_width - self.__radius:
                self.__x = display_width - self.__radius
        elif direction == "LEFT":
            if self.__x > self.__radius:
                self.__x -= self.__speed_x # reduces x value if still on the screen to move left
                  
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_radius(self):
        return self.__radius
    
    def relocate(self, display_height, display_width):
        self.__y = random.randint(0, display_height - self.__radius) # relocates enemy to random x and y coordinates withib the display border and within the radius distance so whole enemy appears on screen 
        self.__x = random.randint(0, display_width - self.__radius)