"""
Execise 5
"""


def fizz_buzz(num):
    """
    Checks if the given number is divisible by 3 and 5. If it is, returns "FizzBuzz".
    If the number is only divisible by 3, returns "Fizz".
    If the number is only divisible by 5, returns "Buzz".
    If the number is not divisible by 3 or 5, returns the number itself.

    Args:
        num (int): The number to be checked.

    Returns:
        str or int: The result of the FizzBuzz calculation.
    """
    # FIX : complete this
    output = ''
    if num % 3 == 0:
        output += 'Fizz'

    if num % 5 == 0:
        output += 'Buzz'

    if output == '':
        return num
    else:
        return output

