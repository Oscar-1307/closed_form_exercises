from functools import lru_cache


@lru_cache(maxsize=None)
def first_function(n: int) -> int:
    """
    Computes the recurrence:
    f(0) = 5
    f(n) = f(n-1) + n^2 for n > 0
    """
    if n == 0:
        return 5

    return first_function(n - 1) + n ** 2


def closed_form(n: int) -> int:
    """
    Computes the closed-form expression:
    5 + n(n + 1)(2n + 1) / 6
    """
    return 5 + (n * (n + 1) * (2 * n + 1)) // 6


def main() -> None:
    n = 8
    print(first_function(n))
    print(closed_form(n))


if __name__ == "__main__":
    main()
