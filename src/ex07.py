"""
Execise 7
"""


def print_ASCII_table(start_char, end_char):
    """
    Generate and print the ASCII table for a range of characters.

    Args:
        start_char (int): The ASCII value of the starting character.
        end_char (int): The ASCII value of the ending character.

    Returns:
        str: Returns nothing. The function simply prints the ASCII characters.

    """
    # FIX : complete this
    ascii_chars = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    chars = ascii_chars[start_char-32:end_char-31]
    for i in chars:
        print(i)
