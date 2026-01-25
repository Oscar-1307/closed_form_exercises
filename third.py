def firstFunction(n):
    result = 1
    if n == 1:
        result = 5
    elif n == 2:
        result = 9
    elif n > 1:
        result = (6*firstFunction(n-1) - 11 *
                  firstFunction(n-2)+6*firstFunction(n-3))
    return result


def Answers(n):
    return(-5+8*2**n-2*3**n)


n = 6
print(firstFunction(n))
print (Answers(n))
