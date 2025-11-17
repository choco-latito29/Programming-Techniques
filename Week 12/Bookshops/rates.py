# --- File: Bookshops/rates.py ---
# This module contains the business logic for rates and penalties.

def get_data_by_category(category):
    """
    Returns a tuple containing (base_rate, penalty_percentage)
    based on the user's category.
    """
    if (category == 'A'):
        # Rate: 0.10, Penalty: 3% (0.03)
        return 0.10, 0.03

    elif (category == 'B'):
        # Rate: 0.12, Penalty: 5% (0.05)
        return 0.12, 0.05

    elif (category == 'C'):
        # Rate: 0.15, Penalty: 7% (0.07)
        return 0.15, 0.07

    elif (category == 'D'):
        # Rate: 0.18, Penalty: 10% (0.10)
        return 0.18, 0.10

    elif (category == 'E'):
        # Rate: 0.20, Penalty: 12% (0.12)
        return 0.20, 0.12