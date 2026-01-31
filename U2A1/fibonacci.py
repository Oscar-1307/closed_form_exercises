import numpy as np


def fibonacciMatrix(number):
    fibonacciMatrix = [
        [1, 1],
        [1, 0]
    ]
    final_sum = []
    while number:
        if (number & 1):
            if not len(final_sum):
                final_sum = fibonacciMatrix
            else:
                final_sum = np.dot(final_sum, fibonacciMatrix)
        fibonacciMatrix = np.dot(fibonacciMatrix, fibonacciMatrix)
        number = number >> 1
    return final_sum[0, 1]


print(fibonacciMatrix(21))
