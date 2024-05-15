#!/usr/bin/python3
"""
Code defining square class and its methods for calculating area and perimeter.
"""


class Square():
    """
    A class representing a square.
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes the square with specified attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculates the area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "{}/{}".format(self.width, self.height)
