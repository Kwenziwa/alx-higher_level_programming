#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            x (int): The x coordinate of the new Rectangle.
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            id (int): The identity of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
        Raises:
            TypeError: If either of x or y is not an int.
            TypeError: If either of width or height is not an int.
            ValueError: If either of x or y < 0.
            ValueError: If either of width or height <= 0.
        """
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        """Set/Get  width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("The width of Rectangle must be an integer")
        if value <= 0:
            raise ValueError("The width of Rectangle must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/Get height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("The height of Rectangle must be an integer")
        if value <= 0:
            raise ValueError("The height of Rectangle must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/Get x coordinate of Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("The x of Rectangle must be an integer")
        if value < 0:
            raise ValueError("The x of Rectangle must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/Get the y coordinate of Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("The y of Rectangle must be an integer")
        if value < 0:
            raise ValueError("The y of Rectangle must be >= 0")
        self.__y = value

    def area(self):
        """Return Rectangle area."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using the character `#`."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        
        if args and len(args) != 0:
            kl = 0
            for arg in args:
                if kl == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif kl == 1:
                    self.width = arg
                elif kl == 2:
                    self.height = arg
                elif kl == 3:
                    self.x = arg
                elif kl == 4:
                    self.y = arg
                kl += 1

        elif kwargs and len(kwargs) != 0:
            for lk, vk in kwargs.items():
                if lk == "id":
                    if vk is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = vk
                elif lk == "width":
                    self.width = vk
                elif lk == "height":
                    self.height = vk
                elif lk == "x":
                    self.x = vk
                elif lk == "y":
                    self.y = vk

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Will return the print() and str() Rectangle representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
