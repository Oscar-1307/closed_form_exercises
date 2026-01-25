from functools import lru_cache


@lru_cache(maxsize=None)
def first_function(n: int) -> int:
    """
    Computes the recurrence relation:
    f(1) = 10
    f(n) = 10*f(n-1) - 25*f(n-2) for n > 1
    """
    if n == 1:
        return 10
    if n <= 0:
        return 1

    return 10 * first_function(n - 1) - 25 * first_function(n - 2)


def closed_form(n: int) -> int:
    """
    Computes the closed-form expression:
    5^n + n*5^n = (1 + n) * 5^n
    """
    return (1 + n) * (5 ** n)


def main() -> None:
    n = 3
    print(first_function(n))
    print(closed_form(n))


if __name__ == "__main__":
    main()
