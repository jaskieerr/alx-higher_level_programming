#!/usr/bin/python3
'''shebang'''


class rectangluangle:
    '''representing rectangluangle'''

    def __init__(self, width=0, height=0):
        '''initilizing a rectangluangle '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets n stes rectangluangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getting and setting the height'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''retuns rectangluangle area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the rectangluangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''represents rectangluangle with # and retuns
        a printable representaion'''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectanglu = []
        for i in range(self.__height):
            [rectanglu.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectanglu.append("\n")
        return ("".join(rectanglu))
    
    def __repr__(self):
        '''the rest'''
        rectanglu = "rectangluangle(" + str(self.__width)
        rectanglu += ", " + str(self.__height) + ")"
        return (rectanglu)
