# Uses python3
import sys

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m
# pisanoperiod
def pisanoperiod(m):
    pre,cur = 0,1
    for i in range(0,m*m):
        # print(pre,cur)
        pre ,cur = cur, (pre+cur)%m
        # print(pre,cur)
        if (pre == 0 and cur == 1):
            return i+1


def get_fibonacci_huge_fast(n,m):

    pisano_period =  pisanoperiod(m)
    print(pisano_period)

    n = n % pisano_period

    pre ,cur  = 0 ,1 
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        pre,cur = cur , pre + cur 
    
    return (cur % m)
 
    # else:
    #     return res
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n,m))
    # get_fibonacci_huge_fast(n,m)
