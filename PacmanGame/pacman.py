import pygame
import random

class Pacman:
    def __init__(self, x, y, radius, colour, speed): # constructor for pacman object 
        self.__x = x # x value instance variable
        self.__y = y # y value instance variable 
        self.__radius = radius 
        self.__colour = colour
        self.__speed_y = speed
        
    def draw(self, display):
        pygame.draw.circle(display, self.__colour, [self.__x, self.__y], self.__radius) # draws pacman object when called using colour and and size coordinates in instance
            
    def move_down(self, display_height): # passes display height parameter to determine y value
        #if self.__y + self.__radius < display_height:
            # add 5 to the self.__y variable
        self.__y = self.__y + 5 # increases y value of pacman each time method is called, moving pacman down 
        if self.__y + self.__radius > display_height: # paremeter to stop pacman from leaving screen, if the y value plus the radius is the bottom of the screen y value pacman relocates to the top. 
            self.__y = 0
            
    def move_up(self, display_height):
        # move pacman up within bounds of screen
        #if self.__y != self.__radius:
        self.__y = self.__y - 5   # reduces y value moving pacman up the screen 
        if self.__y + self.__radius < 0: # if y plus radius is less than zero then pacman still on board 
            self.__y = display_height  # pacman moves to display windoww height value. 
            
    def move_left(self, display_width): # passes x value to control left and right 
        #if self.__x != self.__radius:
        self.__x = self.__x - 5 # pacman moves left 
        if self.__x + self.__radius < 0: # pacman returns to 
            self.__x = display_width
        
    def move_right(self, display_width):
        #if self.__x + self.__radius < display_width:
        self.__x = self.__x + 5
        if self.__x + self.__radius > display_width:# checks if pacman has moved off the right side of the screen 
            self.__x = 0 # returns pacman to left side 
        
    def get_x(self):
        return self.__x #returns x coordinate

    def get_y(self):
        return self.__y# returns y coordinate 
    
    def get_radius(self):
        return self.__radius # returns radius length
    
    def relocate(self, display_height, display_width):
        self.__y = random.randint(0, display_height) # when method is called the coordinates of the pacman are randomised between zero and the display border, relocating pacman 
        self.__x = random.randint(0, display_width)
