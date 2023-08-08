""" Class module"""

class Square:
    """A class representing a Square."""
    
    def __init__(self, size):
        """Initializes the size.
        
        Args:
            size (int): The size of the square.
        """
        if size is not int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
                    
        self.__size = size
