# Uses python3
import sys
from wsgiref.handlers import read_environ

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    
    #write your code here
    # for i in range(0,len(a)):
    #     currentElement = a[i]
    #     count = 0
    #     for j in range(0,len(a)):
    #         if a[j] == currentElement:
    #             count += 1
    #     if count > len(a)//2:
    #         return a[i]
        
    # a.sort()
    # return a[len(a)]
    # print(a)
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
