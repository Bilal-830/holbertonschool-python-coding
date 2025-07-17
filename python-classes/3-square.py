#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Square with size property and area calculation."""

    def __init__(self, size=0):
        """
        Initialize square.

        Args:
            size (int): Length of a side (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size with validation.

        Args:
            value (int): New size value.
        Raises:
            TypeError: If not int.
            ValueError: If < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square."""
        return self.__size ** 2
