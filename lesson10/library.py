import functools


@functools.cache
def exponentiation(n1: int | float, n2: int | float, /, *, expo_num: int | float) -> int | float:
    result = (n1 * n2) ** expo_num
    return result

# assert exponentiation() == int | float, 'not valid data received'
