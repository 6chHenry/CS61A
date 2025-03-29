def draw(hand, positions):
    """Remove and return the items at positions from hand.
    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list( [hand.pop(i) for i in reversorted(positions)] )
