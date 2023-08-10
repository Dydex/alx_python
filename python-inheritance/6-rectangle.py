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

    def __dir__(cls):
        """
        This function removes the __init_subclass (method) from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]
        
        
    
