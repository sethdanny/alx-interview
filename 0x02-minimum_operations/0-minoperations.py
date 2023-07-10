#!/usr/bin/python3
""" minimum operations module"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
      n: The number of H characters to be achieved.

    Returns:
      An integer representing the fewest number of operations needed.
      0 if n is impossible to achieve.
    """

    if n < 2:
        return 0

    operations = 1
    current = 2
    for i in range(2, n + 1):
        if current * 2 <= i:
            operations += 1
            current *= 2
        else:
            operations += 1
            current += current - 1

    return operations
