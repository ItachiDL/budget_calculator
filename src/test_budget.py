import budget

def test_budget():
    # Test the Budget class
    b = budget.Budget(1, 100.0, 'Test')
    print("Amount: ", b.get_amount())
    print("Date: ", b.get_date())
    print("Category: ", b.get_category())
    print("Time: ", b.get_time())
    print("Description: ", b.get_description())

if __name__ == '__main__':
    test_budget()