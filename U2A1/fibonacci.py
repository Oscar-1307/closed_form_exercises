import numpy as np


def fibonacci_matrix(n):
    """Calculate nth Fibonacci number using matrix exponentiation.

    Args:
        n: Non-negative integer position in Fibonacci sequence

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0

    base_matrix = np.array([
        [1, 1],
        [1, 0]],
        dtype=np.int64)
    result = None
    power = base_matrix.copy()

    while n:
        if n & 1:
            result = power if result is None else np.dot(result, power)
        power = np.dot(power, power)
        n >>= 1

    return result[0, 1]


if __name__ == "__main__":
    print(fibonacci_matrix(21))
