def firstFunction(n):
    result = 5
    if n != 0:
        result = (firstFunction(n-1)+(n**2))
    return result


def Answers(n):
    return (5+(n*(n+1)*(2*n+1))/6)


n = 8
print(firstFunction(n))
print(Answers(n))
