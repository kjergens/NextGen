def find_max(a, b, c):
    """
    Get the max of 3 numbers.

    :param a: int, required
    :param b: int, required
    :param c: int, required
    :return: int
    """
    return max((a, b, c))


def multiply_all(nums):
    """
    Multiply all the nums in the tuple
    :param nums: tuple of ints or floats, required
    :return: int or float
    """
    answer = 1
    for n in nums:
        answer *= n
    return answer


def factorial(num):
    """
    Gets the factorial of a number.

    :param num: int, required
    :return: int
    """
    answer = 1
    for n in range(1, num + 1):
        answer = answer * n
    return answer


def factorial_kendrick(n):
    """
    Recursively gets the factorial of a number.

    :param n: int, required
    :return: int
    """
    if n == 0:
        return 1
    else:
        return n * factorial_kendrick(n - 1)


def count_upper_lower(word):
    """
    Counts the uppercase and lowercase letters. Returns a tuple.
    :param word: string, required
    :return: tuple of ints (upper_count, lower_count)
    """
    count_uppers = 0
    count_lowers = 0

    # Go through word and count uppercase and lowercase
    for w in word:
        if w not in '0123456789':  # don't count numbers
            if w == w.lower():
                count_lowers += 1
            else:
                count_uppers += 1
    return count_uppers, count_lowers


def make_unique(t):
    """
    Gets a tuple of unique values.
    :param t: container (tuple, list), required
    :return: tuple
    """
    return tuple(set(t))


def check_prime(num):
    """
    Gets if a number is prime or not.

    :param num: int, required
    :return: boolean, True for prime.
    """
    num = abs(num)  # Take away negative so the math below works. Answer will be same.
    is_prime = False  # For 0 or 1 it's false

    if num > 1:
        is_prime = True  # Assume it's prime, i.e. there's no smaller num that evenly goes in.
        smaller_num = 2  # Don't count 0 or 1 going evenly into it.

        # Stop loop if and when it finds a smaller num that goes in evenly.
        while smaller_num < num and is_prime is True:

            # If there's a smaller num that goes in evenly, it's not prime.
            if num % smaller_num == 0:
                is_prime = False

            smaller_num += 1

    return is_prime


def get_evens(nums):
    """
    Create a tuple of just the even numbers.
    :param nums: container of ints
    :return: a tuple of ints
    """
    t = ()
    for n in nums:
        if n % 2 == 0:  # only add even n
            t = t + (n,)
    return t


# def say_goodbye(name):
#     return "Goodbye, " + name


def say_goodbye(name, times=1):
    """
    Say goodbye a given number of times.

    :param name: string, required
    :param times: int, optional, default=1
    :return: string
    """
    result = 'Goodbye, ' + name + '! '
    return result * times
