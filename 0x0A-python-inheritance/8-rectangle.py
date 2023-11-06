#!/usr/bin/python3
'''shbang'''


class Rectangle(BaseGeometry):
    '''rectangle presentation'''
    def __init__(self, width, height):
        '''rectangle init initilization'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
