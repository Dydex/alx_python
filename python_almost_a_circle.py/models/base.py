"""
This is a modlue for class Base
"""
class Base:
    """
    This is a class Base
    """
    ___nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  
