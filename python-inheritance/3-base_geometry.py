"""
This is module for class Basegeometry.
"""

class Basegeometry:
    """
    This is class Basegeometry.
    """
    def __init__(self):
        self.attribute_name = "Basegeometry"

    
    def __dir__(cls):
        """
        This function removes the __init_subclass (method) from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]

bg = Basegeometry()  
print(bg)
print(dir(bg))