#!/usr/bin/python3
""" This Module define class Square """


class Square:
    """ This Method defines a Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError(" position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ This Method returns the current square area """
    def area(self):
        return self.__size ** 2

    """ This Method prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)

    """ This Method represent the object """
    def __str__(self):
        if self.__size == 0:
            a = ""
        else:
            a = "\n" * self.position[1]
        b = [" " * self.position[0] for i in range(self.__size)]
        c = ["#" * self.__size for i in range(self.__size)]
        b = [x + y for x, y in zip(b, c)]
        return a + "\n".join(b)
