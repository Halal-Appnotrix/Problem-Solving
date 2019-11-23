from heapq import heappop, heappush, heapify
from collections import defaultdict as ddict


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.cost = [ddict(int) for _ in range(vertices)]

    def add_edges(self, src, dest, weight):
        if self.cost[src][dest] and self.cost[dest][src]:
            if self.cost[src][dest] > weight and self.cost[dest][src] > weight:
                self.cost[src][dest] = weight
                self.cost[dest][src] = weight
        else:
            self.cost[src][dest] = weight
            # Becouse, Given Graph is undirected.
            self.cost[dest][src] = weight


    def dijkstra(self, source):
        
        Q = [(0, source)]
        visited = [False] * self.v
        distance = [-1] * self.v 
        distance[source] = 0
        heapify(Q)

        while Q:

            min_dist, u = heappop(Q)
    

            if not visited[u]:
                for v in self.cost[u]:
                    if distance[v] == -1:
                        distance[v] = min_dist + self.cost[u][v]
                    else:
                        distance[v] = min(distance[v], min_dist+self.cost[u][v])
                    heappush(Q, (distance[v], v))
                visited[u] = True

        return distance[:source] + distance[source+1:]


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        g = Graph(n)

        for _ in range(m):
            src, dest, w = list(map(int, input().split()))
            g.add_edges(src-1, dest-1, w)

        s = int(input())

        result = g.dijkstra(s-1)

        print(' '.join(map(str, result)))
    print()
