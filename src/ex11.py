"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    hours = tsec // 3600
    minutes = (tsec - (3600 * hours)) // 60
    seconds = tsec - (3600 * hours) - (60 * minutes)

    hours_text = '' if hours == 0 else f'{hours}h '
    minutes_text = '' if minutes == 0 else f'{minutes}m '
    seconds_text = f'{seconds}s'
    if seconds == 0 and (minutes != 0 or hours != 0):
        seconds_text = ''

    return f'{hours_text}{minutes_text}{seconds_text}'.strip()
