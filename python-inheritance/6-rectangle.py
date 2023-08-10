"""
This is module for class Basegeometry.
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry
                
class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """
    
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [
            item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
        
        
    
