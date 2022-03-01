# Uses python3
import sys

# from numpy import append

def optimal_summands(n):
    summands = []
    ot = n
    if n == 1:
        summands.append(ot)
        # quit()
    
    for i in range(1,n):
        if ot > 2*i:
            summands.append(i)
            ot -= i
        else:
            summands.append(ot)
            break
    
    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
