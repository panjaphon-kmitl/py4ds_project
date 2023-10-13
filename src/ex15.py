"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    num_list = sorted(num_list)
    if num_list == []:
        return None
    else:
        length = len(num_list)
        if length % 2 == 0:
            end = int((length / 2))
            start = end - 1
            return (num_list[start] + num_list[end]) / 2
        elif length % 2 == 1:
            mid = int((length - 1) / 2)
            return num_list[mid]
