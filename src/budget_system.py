"""
This module contains the BudgetSystem class which is responsible for managing the budget system.

Author: ItachiDL
Date: 10. Juli 2024
Version: 0.1
"""

from budget import Budget
from database import Database

class BudgetSystem:
    def __init__(self):
        self.__budget_database = Database()
        self.__budget_database.create_table('budget')

    def add_budget(self):
        category = int(input("Enter the category of the budget entry: "))
        amount = float(input("Enter the amount of the budget entry: "))
        description = input("Enter the description of the budget entry: ")
        budget = Budget(category, amount, description)
        self.__budget_database.insert_budget(budget)

    def get_all_budgets(self):
        """
            Retruns an tupel with the entries of the budget database.
            1. id
            2. category
            3. amount
            4. date
            5. time
            6. description

            Returns:
                budgets (list): A list of Budget objects.
        """
        budgets = []
        returns = self.__budget_database.get_all_budgets()
        for budget in returns:
            bud = Budget(budget[1], budget[2], budget[5])
            bud.set_date_database(budget[3])
            bud.set_time_database(budget[4])
            bud.set_id(budget[0])
            budgets.append(bud)

        return budgets

    def print_all_budgets(self):
        budgets = self.get_all_budgets()
        for budget in budgets:
            print("ID: ", budget.get_id())
            print("Category: ", budget.get_category())
            print("Amount: ", budget.get_amount())
            print("Date: ", budget.get_date())
            print("Time: ", budget.get_time())
            print("Description: ", budget.get_description())
            print()




if __name__ == '__main__':
    b = BudgetSystem()
    b.print_all_budgets()







