#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(10, 8, 3, 6)
    dictionary1 = r1.to_dictionary()
    dictionary2 = r2.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary1, dictionary2])
    print(dictionary1)
    print(type(dictionary1))
    print(dictionary2)
    print(type(dictionary2))
    print(json_dictionary)
    print(type(json_dictionary))
