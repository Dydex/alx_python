"""
This is module for class Basegeometry.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
"""
import a file with nmber and put it in variable called Basegeometry.
"""

class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """
    
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def __dir__(cls) -> None:
             attributes = super().__dir__()
             return [x for x in attributes if x != '__init_subclass__']
    
