"""
Budget Management Module

This module provides a class for managing budget entries, including income, outcomes, and transfers.

Author: ItachiDL
Date: 10. Juli 2024
Version: 0.1
"""
from datetime import datetime


class Budget:
    """
    A class to store a budget entry.
    """

    def __init__(self, category, amount, description=None):
        """
        Args:
            category (int): Descript what the Budget is.
                - 1: Income
                - 2: Outcome
                - 3: Transfer
                - 4: Unknown
            amount (float): The amount of the budget entry.

        Attributes:
            date (str): The date of the budget entry in the format 'YYYY-MM-DD'.
            time (str): The time of the budget entry in the format 'HH:MM:SS:mmm'.
            description (str): A description of the budget entry.
            id (int): The id of the budget entry.

        """
        assert type(amount) == float, "Amount must be a float"
        assert type(category) == int, "Category must be an integer"

        self.__amount = amount
        self.set_date()
        self.__category = category
        self.set_time()
        self.__description = description
        self.__id = None

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        assert type(amount) == float, "Amount must be a float"
        self.__amount = amount

    def get_date(self):
        return self.__date

    def set_date(self):
        # get the current date in format YYYY:MM:DD
        self.__date = datetime.now().strftime('%Y:%m:%d')

    def set_date_database(self, date):
        """
        Set the date of the budget entry.
        :param date: str the date of the budget entry in the format 'YYYY-MM-DD'
        """
        # Convert date string to datetime object
        try:
            self.__date = datetime.strptime(date, '%Y:%m:%d')
        except ValueError:
            raise ValueError('Incorrect date format, should be YYYY:MM:DD but is ' + date)

    def get_category(self):
        return self.__category

    def set_category(self, category):
        assert type(category) == int, "Category must be an integer"
        self.__category = category

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_time(self):
        return self.__time

    def set_time(self):
        """
        Get called when the class is initialized. It set the current time.

        Attributes:
            time (str): The time of the budget entry in the format 'HH:MM:SS:mmm'.

        """
        current_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]
        self.__time = current_time

    def set_time_database(self, time):
        """
        Set the time of the budget entry.
        :param time: str the time of the budget entry in the format 'HH:MM:SS:mmm'
        """
        # Convert time string to datetime object
        try:
            self.__time = datetime.strptime(time, '%H:%M:%S:%f')
        except ValueError:
            raise ValueError('Incorrect time format, should be HH:MM:SS:mmm but is ' + time)

    def get_id(self):
        return self.__id

    def set_id(self, id_system):
        self.__id = id_system

