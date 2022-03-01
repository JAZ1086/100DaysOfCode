# Uses python3
import sys

def get_change(m):
    #write your code here
    #number  of coins
    numbCoins = 0

    while (m  > 0):
        if m >= 10:
            m = m - 10
            numbCoins = numbCoins +1
        elif m >= 5:
            m = m - 5
            numbCoins = numbCoins +1
        elif m <5:
            m  =  m  - 1
            numbCoins = numbCoins +1

    return numbCoins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
