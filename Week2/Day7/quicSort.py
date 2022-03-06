
#  function to find the partition postion
def partition(n,low,high):

    pivot = n[high]

    i = low -1

    for j in range(low,high):
        if n[j] <= pivot :
            i = i + 1
            (n[i],n[j]) = (n[j],n[i])
    
    (n[i+1],n[high]) = (n[high] ,n[i+1])

    return i+1


def quickSort(n,low,high):

    if low < high:
        pi = partition(n,low,high)
        print("PI: "+ str(pi))
        quickSort(n,low,pi-1)
        quickSort(n,pi +1,high)



data = [6,5,12,3,10,9,1]
print(data)

size = len(data)

quickSort(data, 0, size -1)

print(data)


