"""
Exercise 24 : Every 15 minutes, ante meridiem (am) and post meridiem (pm)
ante : before
post : after
meridiem : midday
"""


def get_time_every_15_min():
    """
    Generate a time string every 15 minutes.

    This function iterates through the meridiems, hours, and minutes to generate a time string
    for every 15 minutes. It prints the time string in the format "hour:minute meridiem".

    Returns:
        str: The generated time string.
    """
    # FIX : complete this
    out = """"""
    for suffix in ['am', 'pm']:
        hour = 0
        minutes = ['00', '15', '30', '45']
        while hour < 12:
            for i in minutes:
                if hour == 0:
                    print(f'12:{i} {suffix}')
                else:
                    print(f'{hour}:{i} {suffix}')
            hour += 1
