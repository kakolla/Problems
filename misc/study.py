

arr = [1,2,3,4]
arr.append(4)


def bin_search(arr, val):
    l = 0
    r = len(arr) - 1

    while (l <= r):
        mid = (l+r)//2

        if (arr[mid] == val):
            return mid
        elif (arr[mid] < val):
            l = mid +1
        elif (arr[mid] > val):
            r = mid-1
    
    return -1


if "__main__" == __name__:
    # arr
    arr = []

    # set 
    milk = set()

    # dict/hashmap
    milk2 = {}

    # stack
    st = []
    st.append(3)
    st.append(4)
    st.append(8)
    st.append(10)
    st.pop()


    # queue
    from collections import deque
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.popleft()

    # priority queue
    import heapq
    pq = []
    heapq.heappush(pq, 3)
    heapq.heappush(pq, 10)
    heapq.heappush(pq, 1)

    import random
    arr = [random.randint(0, 10) for x in range(10)]
    arr.sort()
    print(arr)
    to_find = arr[6]  
    print(to_find)
    print(bin_search(arr, to_find))

    # maxheap
    print("max heap:")
    import heapq
    pq = []
    heapq.heappush(pq, -3)
    heapq.heappush(pq, -2)
    heapq.heappush(pq, -0)
    heapq.heappush(pq, -10)
    heapq.heappush(pq, -1)
    print("largest is: ")
    print(-heapq.heappop(pq))

    # dict with safe access
    print("map with safe access")
    mp = {}
    print(mp.get(0, -1)) # 2nd param is default value

    








    