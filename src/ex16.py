"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    if num_list == []:
        return None
    else:
        num_set = set(num_list)

        freq = [num_list.count(i) for i in num_set]
        max_freq = max(freq)
        max_index = freq.index(max_freq)

        max_num = list(num_set)[max_index]

        return max_num
