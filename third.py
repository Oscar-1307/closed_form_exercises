from functools import lru_cache


@lru_cache(maxsize=None)
def first_function(n: int) -> int:
    """
    Computes the value of the recurrence relation:
    f(1) = 5
    f(2) = 9
    f(n) = 6*f(n-1) - 11*f(n-2) + 6*f(n-3) for n > 2
    """
    if n == 1:
        return 5
    if n == 2:
        return 9
    if n <= 0:
        return 1

    return (
        6 * first_function(n - 1)
        - 11 * first_function(n - 2)
        + 6 * first_function(n - 3)
    )


def closed_form(n: int) -> int:
    """
    Computes the closed-form solution:
    -5 + 8*2^n - 2*3^n
    """
    return -5 + 8 * (2 ** n) - 2 * (3 ** n)


def main() -> None:
    n = 6
    print(first_function(n))
    print(closed_form(n))


if __name__ == "__main__":
    main()
