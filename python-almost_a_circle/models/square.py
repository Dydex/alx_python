"""
This is a square module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a square class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the initialization method
        """
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        """ str magic method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        getter method for width.
        """
        return self.size

    @size.setter
    def size(self, value):
        """
        setter method for width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.size = value
