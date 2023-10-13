"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(bottles):
    """
    Calculate the number of bottles of beer on the wall.
    And print out like this :

    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall,
    1 bottle of beer.
    Take one down, pass it around,
    No more bottles of beer on the wall!

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    # FIX : complete this
    for i in range(bottles):
        s = '' if i == bottles-1 else 's'
        if i == bottles-1:
            suffix = f'No more bottles of beer on the wall!'
        else:
            suffix = f'{bottles-i-1} bottle{s} of beer on the wall.'

        return f"""{bottles-i} bottle{s} of beer on the wall,
{bottles-i} bottle{s} of beer.
Take one down, pass it around,
{suffix}
"""


def loop_bottles_of_bears(bottle):
    while bottle > 0:
        print(bottles_of_beer(bottle))
        bottle -= 1


if __name__ == '__main__':
    loop_bottles_of_bears(5)
