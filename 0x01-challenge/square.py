#!/usr/bin/python3
"""
Code defining square class and its methods for calculating area and perimeter.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        width (int): The width of the square.
    """

    def __init__(self, **kwargs):
        """
        Initializes the square with specified attributes.

        Args:
            **kwargs: Arbitrary keyword arguments to set attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return self.width * 4

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: String representation of the square's width.
        """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """
    Main function to demonstrate usage of the Square class.
    """
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
