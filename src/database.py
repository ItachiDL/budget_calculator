
"""
Budget Database Management Module

This modul provides a class for managing budget entries in a database.

Author: ItachiDL
Date: 10. Juli 2024
Version: 0.1
"""

import sqlite3
from budget import Budget

class Database:
    """
    A class to manage a budget database. It takes a sqlite3 connection object as input.
    """
    def __init__(self):
        """
        Initialize the database connection.

        Attributes:
            conn (sqlite3.Connection): The connection to the database.
            cursor (sqlite3.Cursor): The cursor to the database.
        """
        self.__conn = sqlite3.connect('budget_texes.db')
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        """
        Close the database connection.
        """
        self.__conn.close()

    def create_table(self, switch):
        """
        Create the budget table in the database.
        """
        if switch == 'budget':
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS budget
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    category INTEGER,
                                    amount REAL,
                                    date TEXT,
                                    time TEXT,
                                    description TEXT)''')
            self.__conn.commit()
        elif switch == 'taxes':
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS taxes
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    category INTEGER,
                                    amount REAL,
                                    date TEXT,
                                    time TEXT,
                                    description TEXT)''')
            self.__conn.commit()
        else:
            # raise an error if the switch is not valid
            raise ValueError('Invalid switch value')

    def insert_budget(self, budget):
        """
        Insert a budget entry into the database.

        Args:
            budget (Budget): The budget entry to insert.
        """
        self.__cursor.execute('''INSERT INTO budget (category, amount, date, time, description)
                                VALUES (?, ?, ?, ?, ?)''',
                                (budget.get_category(), budget.get_amount(), budget.get_date(), budget.get_time(), budget.get_description()))
        self.__conn.commit()

    def insert_tax(self, tax):
        """
        Insert a tax entry into the database.

        Args:
            tax (Tax): The tax entry to insert.
        """
        self.__cursor.execute('''INSERT INTO taxes (category, amount, date, time, description)
                                VALUES (?, ?, ?, ?, ?)''',
                                (tax.get_category(), tax.get_amount(), tax.get_date(), tax.get_time(), tax.get_description()))
        self.__conn.commit()

    def get_budget_by_id(self, id_number):
        """
        Get a budget entries by the id from the database.

        Args:
            id_number (int): The id of the budget entry to get.

        Returns:
            list: A list of budget entries.
        """
        self.__cursor.execute('SELECT * FROM budget WHERE id = ?', (id_number,))
        return self.__cursor.fetchall()

    def get_taxes(self):
        """
        Get all tax entries from the database.

        Returns:
            list: A list of tax entries.
        """
        self.__cursor.execute('SELECT * FROM taxes')
        return self.__cursor.fetchall()

    def delete_budget(self, id):
        """
        Delete a budget entry from the database.

        Args:
            id (int): The id of the budget entry to delete.
        """
        self.__cursor.execute('DELETE FROM budget WHERE id = ?', (id,))
        self.__conn.commit()

    def delete_tax(self, id_number):
        """
        Delete a tax entry from the database.

        Args:
            id (int): The id of the tax entry to delete.
        """
        self.__cursor.execute('DELETE FROM taxes WHERE id = ?', (id_number,))
        self.__conn.commit()

    def update_budget(self, id_number, budget):
        """
        Update a budget entry in the database.

        Args:
            id (int): The id of the budget entry to update.
            budget (Budget): The new data for the budget entry.
        """
        # Check if the budget entry exists
        self.__cursor.execute('SELECT * FROM budget WHERE id = ?', (id_number,))
        if not self.__cursor.fetchone():
            raise ValueError("Budget entry not found")

        # Update the budget entry
        self.__cursor.execute('''UPDATE budget SET category = ?, amount = ?, date = ?, time = ?, description = ?
                                WHERE id = ?''',
                                (budget.get_category(), budget.get_amount(), budget.get_date(), budget.get_time(), budget.get_description(), id))
        self.__conn.commit()

    def tax_update(self, id, tax):
        """
        Update a tax entry in the database.

        Args:
            id (int): The id of the tax entry to update.
            tax (Tax): The new data for the tax entry.
        """
        # Check if the tax entry exists
        self.__cursor.execute('SELECT * FROM taxes WHERE id = ?', (id,))
        if not self.__cursor.fetchone():
            raise ValueError("Tax entry not found")

        # Update the tax entry
        self.__cursor.execute('''UPDATE taxes SET category = ?, amount = ?, date = ?, time = ?, description = ?
                                WHERE id = ?''',
                                (tax.get_category(), tax.get_amount(), tax.get_date(), tax.get_time(), tax.get_description(), id))
        self.__conn.commit()

    def get_all_budgets(self):
        """
        Get all budget entries from the database.
        :return:
            All Budget entries in the database
        """
        self.__cursor.execute('SELECT * FROM budget')
        return self.__cursor.fetchall()





