def add_one(number):
    return number + 1


class Foo:
    """
    A generic class that depends on add_one
    """

    def __init__(self, number):
        self._num = number
        self._num2 = add_one(number)
