import numpy as np


def power_matrix(matrix, n):
    """Recursively compute matrix power using divide and conquer.

    Args:
        matrix: 2x2 numpy array
        n: Positive integer exponent

    Returns:
        matrix^n as numpy array
    """
    if n == 1:
        return matrix

    half = power_matrix(matrix, n // 2)
    half = np.dot(half, half)
    return half if n % 2 == 0 else np.dot(half, matrix)


def fibonacci_matrix(n):
    """Calculate nth Fibonacci number using recursive matrix exponentiation.

    Args:
        n: Positive integer position in Fibonacci sequence

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is not positive
    """
    if n <= 0:
        raise ValueError("n must be positive")

    base_matrix = np.array([
        [1, 1],
        [1, 0]],
        dtype=np.int64)
    return power_matrix(base_matrix, n)[0, 1]


if __name__ == "__main__":
    print(fibonacci_matrix(21))
