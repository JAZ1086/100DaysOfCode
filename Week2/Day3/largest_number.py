#Uses python3

# from asyncio.windows_events import NULL
import sys

def isBetter(number,maxNumber):
    # print("Number:  "+ str(number) + " MaxNumber: "+ str(maxNumber))
    return int(str(number)+str(maxNumber)) >= int(str(maxNumber)+str(number))

def largest_number(a):
    #write your code here
    res = ""
    while  a!=[] :
        maxValue = 0
        for x in a:
            if isBetter(x,maxValue):
                maxValue = x
        res+=maxValue
        a.remove(maxValue)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
