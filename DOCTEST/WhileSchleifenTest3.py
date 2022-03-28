import doctest


def while_schleife_3(maximum):
    """
    >>> while_schleife_3(10)
    8
    >>> while_schleife_3(20)
    16
    >>> while_schleife_3(2)
    1
    >>> while_schleife_3(1)
    1
    >>> while_schleife_3(100)
    64
    """
    wert = 1
    while True:
        if wert * 2 < maximum:
            wert = wert * 2
        else:
            break
    return wert


if __name__ == "__main__":
    doctest.testmod()
