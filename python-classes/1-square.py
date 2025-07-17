#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Square with private size and area method."""

    def __init__(self, size=0):
        """
        Initialize square.

        Args:
            size (int): Length of a side (default 0).
        Raises:
            TypeError: If size not int.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return area of square.

        Returns:
            int: area
        """
        return self.__size ** 2
