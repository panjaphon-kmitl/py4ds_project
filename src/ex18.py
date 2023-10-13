"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(cups, price_each):
    if cups == 0:
        return 0
    else:
        free_cups = (cups-1) // 8
        not_free_cups = cups - free_cups
        return not_free_cups  * price_each
