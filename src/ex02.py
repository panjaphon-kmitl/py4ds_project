"""
Execise 2
"""


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # TODO : complete this
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit


def convert_to_celsius(f):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # TODO : complete this
    c = (f - 32) * (5/9)
    return c
