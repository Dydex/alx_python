""" This is a square(object) module.  """

class Sqaure:
    """ 
    A class representing a Square.
    # class Square
    Attributes:
    __size = size of the square.
    """ 
    
    def __init__(self, size):
        """ Initializes the size.
        """
        if size is not int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
                    
        self.__size = size
