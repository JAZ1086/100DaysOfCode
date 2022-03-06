def binary_search(keys, query):
    # write your code here
    lt  = 0
    rt = len(keys) -1

    while (lt <= rt):
        mid = (int)(lt + (rt - lt)//2)
        # if keys[lt] == keys[lt +1]:
        #     lt = lt + 1
        if keys[mid] == query:
            for i in range(lt ,rt):
                 if keys[i] == keys[i]:
                     continue
            return mid
        elif keys[mid] < query:
            lt = mid + 1
        else:
            rt = mid - 1
    return -1


    # while l != r:
    #     mid = l + (r - l)/2
    #     if keys[mid] <
    # # pass


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
