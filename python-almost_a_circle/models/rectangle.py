"""
This is a module for class Base
"""

from base import Base
"""
This imports the class base
"""


class Recangle(Base):
    """
    This is class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the initialization method
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter method for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width.
        """
        self.__width = value

    @property
    def height(self):
        """
        getter method for height.
        """
        return self.__height

    @width.setter
    def height(self, value):
        """
        setter method for height.
        """
        self.__height = value

    @property
    def x(self):
        """
        getter method for x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x.
        """
        self.__x = value

    @property
    def y(self):
        """
        getter method for y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y.
        """
        self.__y = value
