# Uses python3
from cgi import print_directory
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
# def get_fibonacci_last_digit_fast(n):
#     res = {0:0,1:1}

#     for i in range(2,n+1):
#         res[i] = (res[i-1]+ res[i-2])%10
    
#     return res[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(get_fibonacci_last_digit_naive(n))
    # print(get_fibonacci_last_digit_fast(n))
