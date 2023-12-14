#!/usr/bin/python3
""" This Module for Rectangle """
from models.base import Base


class Rectangle(Base):
    """ This Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def display(self):
        """ This method to display rectangle with # """
        for blankline in range(self.y, 0, -1):
            print()
        for col in range(self.height, 0, -1):
            for space in range(self.x, 0, -1):
                print(" ", end="")
            for row in range(self.width, 0, -1):
                print("#", end="")
            print()

    def __str__(self):
        """ This method return the class representation """
        x = "[Rectangle] ({}) {}/{} ".format(self.id, self.x, self.y)
        x += "- {}/{}".format(self.width, self.height)
        return x

    def update(self, *args, **kwargs):
        """ This method update the instance attributes"""
        if kwargs and (not args or args is None):
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i, value in enumerate(args):
                setattr(self, ['id', 'width', 'height', 'x', 'y'][i], value)

    def to_dictionary(self):
        """ This mehtod returns the dictionary representation """
        dic1 = ['x', 'y', 'id', 'height', 'width']
        dic2 = [self.x, self.y, self.id, self.height, self.width]
        return dict(zip(dic1, dic2))
