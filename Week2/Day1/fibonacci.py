# Uses python3
# res = {0:0,1:1}
# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)


# using memorization to store already calculated values
res = {0:0,1:1}
def calc_fib(n):
    if n in res:
        return res[n]
    
    res[n] = calc_fib(n-1) + calc_fib(n-2)
    return res[n]

n = int(input())
print(calc_fib(n))
