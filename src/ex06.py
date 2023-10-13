"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # FIX : complete this
    str_num = str(num)

    if str_num.endswith('11') or str_num.endswith('12') or str_num.endswith('13'):
        return str_num + 'th'
    elif str_num.endswith('1'):
        return str_num + 'st'
    elif str_num.endswith('2'):
        return str_num + 'nd'
    elif str_num.endswith('3'):
        return str_num + 'rd'
    else:
        return str_num + 'th'
