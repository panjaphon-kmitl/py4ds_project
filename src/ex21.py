"""
Exercise 21 : Validate Date
"""


def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    from src.ex20 import is_leap_year

    # FIX : complete this
    leap_year_day = is_leap_year(year)

    # check zero as output
    if month == 0 or day == 0:
        return False

    if month == 2:
        return day <= 28 + leap_year_day
    elif month in (1,3,5,7,8,10,12):
        return day <= 31
    elif month in (4,6,9,11):
        return day <= 30
    else:
        return False