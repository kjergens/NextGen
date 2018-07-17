def make_double(a):
    """
    Make a number double
    :param a: int, required
    :return: int
    """
    dbl = a * 2
    return dbl  # return value


def make_half(a):
    """
    Halve a number
    :param a: int
    :return: float
    """
    h = a / 2
    return h


def make_plural(word):
    """
    Adds 's' to end of word
    :param word: string
    :return: string
    """
    return word + 's'


def get_power(base, exp):
    """
    Raise base to the power of exp
    :param base: int
    :param exp: int
    :return: int
    """
    return base ** exp


print(get_power(8, 2))

print(make_plural('hat'))

b = make_double(5)
print(b)
b = make_half(8)
print(b)
