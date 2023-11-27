#!/usr/bin/python3
""" This Module defines rectangle """


class Rectangle():
    """ Defines a Rectangle class """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ This method returns the area """
    def area(self):
        return self.__height * self.__width

    """ This method returns the perimeter """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    """ This method return informal string for object representation """
    def __str__(self):
        a = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                if i > 0:
                    a += "\n"
                a += "#" * self.__width
        return a

    """ This method return formal string for object representation """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """ This method delete instance """
    def __del__(self):
        print("Bye rectangle...")
