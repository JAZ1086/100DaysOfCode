# from operator import le
# import re
# from turtle import right


def binary_search(keys, query):
    # write your code here
    # n = keys[0]
    # seq = keys[1:]

    lt  = 0
    rt = len(keys) -1

    while (lt <= rt):
        mid = (int)(lt + (rt - lt)//2)
        # if keys[lt] == keys[lt +1]:
        #     lt = lt + 1
        if query > keys[mid]:
            lt = mid +1 
        elif query < keys[mid]:
            rt = mid -1
        else:
            return mid
    return -1


    # pass
    # # print(keys)
    # # print(query)


if __name__ == '__main__':
    num_keys = int(input())
    # print(num_keys)
    input_keys = list(map(int, input().split()))
    # print(input_keys)
    assert len(input_keys) == num_keys

    num_queries = int(input())
    # print(num_queries)
    input_queries = list(map(int, input().split()))
    # print(input_queries)
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
