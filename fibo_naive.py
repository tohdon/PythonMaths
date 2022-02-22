
def fibo_naive(n):
    if n<=1:
        return n
    return fibo_naive(n-1) + fibo_naive(n-2)

result = fibo_naive(9)
print(result)    