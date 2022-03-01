# python3
import sys


def compute_min_refills(distance,tank,n,stops):
    # write your code here
    numberOfRefils = 0
    currentRefil = 0
    currentMiles = tank
    while currentMiles <= distance:
        if currentRefil >=n or stops[currentRefil]>currentMiles:
            return -1
        
    #     lastRefill = currentRefil
        while (currentRefil< n-1 and stops[currentRefil +1]<= currentMiles):
              currentRefil +=1
        
    #     if currentRefil == lastRefill:
    #         return -1
        
    #     if currentRefil <= tank:
        numberOfRefils +=1
        # print(currentMiles)
        currentMiles = stops[currentRefil] +tank
        # print(currentMiles)
        currentRefil +=1
        # print(currentMiles)

    return numberOfRefils

if __name__ == '__main__':
    d, m,n, *stops = map(int, sys.stdin.read().split())
    # print(d)
    # print(m)
    # print(stops)
    print(compute_min_refills(d, m,n,stops))
