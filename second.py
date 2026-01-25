def firstFunction(n):
    result = 1
    if n == 1:
        result = 10
    elif n > 1:
        result = (10*firstFunction(n-1)-25*firstFunction(n-2))
    return result


def Answers(n):
    print((5**n) + (n*(5**n)))
    print((5**n)*(1+n))


n = 3
print(firstFunction(n))
Answers(n)
