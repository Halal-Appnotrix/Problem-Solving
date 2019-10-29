from heapq import heappush, heappop

class Solution(object):
    def minimumAverage(customers, n):

        customers = sorted(customers)[::-1]
        heap, w_time, c_time = [], 0, 0

        while customers or heap:
            while customers and customers[-1][0] <= c_time:
                heappush(heap, customers.pop()[::-1])

            if heap:
                c_customer = heappop(heap)
                c_time += c_customer[0]
                w_time += c_time - c_customer[1]
                print(w_time)
            else:
                heappush(heap, customers.pop()[::-1])
                c_time = heap[0][1]

        return (w_time // n)
    
if __name__ == '__main__':

    n = int(input())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = Solution.minimumAverage(customers, n)

    print(str(result) + '\n')
