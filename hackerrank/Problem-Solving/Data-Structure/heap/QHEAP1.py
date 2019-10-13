'''
    Problem Link:-https://www.hackerrank.com/challenges/qheap1/problem
    It able to pass all test case given the time.
'''
from heapq import heappush, heappop

heap = []
deleted_items = set()
n = int(input())
for _ in range(n):
    query = input()

    if query[0] is '1':
        q, item = list(map(int, query.split()))
        heappush(heap, item)
        deleted_items.add(item)
    elif query[0] is '2':
        q, item = list(map(int, query.split()))
        deleted_items.discard(item)
    elif query[0] is '3':
        while heap[0] not in deleted_items:
            heappop(heap)

        print(heap[0])
