#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """A class representing a square.

       Attributes:
           size (int): The size of the square's side.

       Methods:
           __init__: Initializes a Square instance.
           size: Getter method to retrieve the size of the square.
           size.setter: Setter method to set the size of the square.
           area: Calculates the area of the square.
       """

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square's side (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

       Args:
           value (int): The size of the square's side.

       Raises:
           TypeError: If the value is not an integer.
           ValueError: If the value is less than 0.
       """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

       Returns:
           int: The area of the square (size squared).
       """
        return self.__size ** 2
