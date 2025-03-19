import pygame, random

class Food:
  
    __colour = [255, 0, 0] # class variables of the food colour and dimensions 
    __width = 15
    __height = 15

    def __init__(self, x, y):
        self.__x = x # instance of coordinates 
        self.__y = y
    
    def draw(self, display):
        pygame.draw.rect(display, self.__colour, [self.__x, self.__y, self.__width, self.__height]) # draws a rectangle as the food with the instances dimensions
    
    def relocate(self, display_height, display_width):
        self.__y = random.randint(0, display_height - self.__height) # coordinates are randomised when called to relocate the food, height and width taken away from display border to ensure whole food area is within the borders 
        self.__x = random.randint(0, display_width - self.__width)
        
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def get_size(self):
        return [self.__width, self.__height] # this returns the size of the food in a list format