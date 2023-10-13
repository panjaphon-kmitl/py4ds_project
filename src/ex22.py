"""
Exercise 22 : Rock Paper Scissor
"""


def rps_check(p1, p2):
    """
    Check the result of a rock-paper-scissors game between two players.

    Parameters:
        p1 (str): The choice of player one. It can be 'rock', 'paper', or 'scissor'.
        p2 (str): The choice of player two. It can be 'rock', 'paper', or 'scissor'.

    Returns:
        str: The result of the game. It can be 'player one', 'player two', or 'tie'.
    """
    # FIX : complete this
    selected = [p1, p2]
    map = {p1:'player one', p2:'player two'}

    if p1 == p2:
        return 'tie'
    elif 'rock' in selected and 'paper' in selected:
        return map['paper']
    elif 'rock' in selected and 'scissors' in selected:
        return map['rock']
    elif 'paper' in selected and 'scissors' in selected:
        return map['scissors']


