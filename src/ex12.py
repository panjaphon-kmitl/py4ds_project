"""
Execise 12
"""


def get_smallest(num_list):
    """
    Get the smallest number from a list of numbers.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """
    return None if num_list == [] else min(num_list)
