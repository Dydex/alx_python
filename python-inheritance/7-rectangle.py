"""
This is a rectangle object module
"""

BaseGeometry = __import__('6-rectangle').BaseGeometry
"""
import a file with nmber and put it in variable called Basegeometry
"""

class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """
    
    def area(self):
        area = self.__width * self.__height
        return area
    
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.height)) 
    