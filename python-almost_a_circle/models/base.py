"""
This is a modlue for class Base
"""
class Base:
    """
    This is a class Base
    """
    ___nb_objects = 0

    def __init__(self, id=None):
        """
        This is an initialization method.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects  

