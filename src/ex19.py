"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(length):
    # TODO : complete this
    min_length = 12
    length = max(length, min_length)
    pwd = ''
    # required chars
    chars_set = [LOWER_LETTERS, UPPER_LETTERS, NUMBERS, SPECIAL]
    for i in chars_set:
        pwd += random.choice(i)

    # random so the output doesn't have prefix pattern
    pwd = list(pwd)
    random.shuffle(pwd)
    pwd = ''.join(pwd)

    # other chars
    for i in range(length - len(chars_set)):
        pwd += random.choice(ALL_CHARS)

    return pwd


