"""
This is module for class Basegeometry.
"""
class BaseMetaClass(type):
    """
    This is a BaseMetaClass
    """
    
    
    def __dir__(cls):
        """
        This function removes the __init_subclass (method) from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]

class BaseGeometry(metaclass=BaseMetaClass):
        """
        This is class BaseGeometry.
        """
        
        def __dir__(cls):
            """
            This function removes the __init_subclass (method) from the default method inherited from the parent class
            """
            return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]

        def area(self):
            raise Exception ("area() is not implemented")

        def integer_validator(self, name, value):
            self.name = name
            if type(value) is not int:
                raise TypeError (f"{name} must be an integer")
            if value <= 0:
                raise ValueError (f"{name} must be greater than 0")
                
class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """
    
class rectangle(Rectangle):
    """
    This is a class Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def __dir__(cls) -> None:
        attributes = super().dir__()
        return [x for x in attributes if x != '__init_subclass__']