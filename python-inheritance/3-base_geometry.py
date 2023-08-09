"""
This is module for class Basegeometry.
"""

class BaseGeometry:
    """
    This is class BaseGeometry.
    """
    
    def __dir__(cls):
        """
        This function removes the __init_subclass (method) from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]
BaseGeometry()
