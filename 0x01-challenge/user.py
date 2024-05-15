#!/usr/bin/python3
"""
User class for managing user data.
"""


class User():
    """ A class representing a user. """

    def __init__(self):
        """ Initializes a new User object. """
        self.__email = None

    @property
    def email(self):
        """ Get the email address of the user. """
        return self.__email

    @email.setter
    def email(self, value):
        """ Set the email address of the user. """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """
    Main function to demonstrate usage of the User class.
    """
    u = User()
    u.email = "john@snow.com"
    print(u.email)
