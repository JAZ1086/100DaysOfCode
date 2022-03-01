# Uses python3
import re
import sys

def get_optimal_value(capacity, weights, values):
    
    value = 0
    #write your code here
    lt = list(range(len(values)))
    # Calculate the ratio value weigth
    ratio = [val/wt for val,wt in zip(values,weights)]
    # print(ratio)
    # store the index of each ratio in a list
    lt.sort(key=lambda i : ratio[i],reverse=True)
    #print(lt)
    for i in lt:
        if weights[i]<=capacity:
            value += values[i]
            # print(value)
            capacity -= weights[i]
            # print(capacity)
        else:
            value += values[i]*capacity/weights[i]
            break
    # print(ratio)
    # print(lt)

    # while capacity>0:
    #     pass
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # print(data)
    n, capacity = data[0:2]
    # print(n,capacity)
    values = data[2:(2 * n + 2):2]
    # print(values)
    weights = data[3:(2 * n + 2):2]
    # print(weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
