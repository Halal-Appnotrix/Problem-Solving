def getWays(n, c):
    size = n+1
    ways = [0]*size

    ways[0] = 1
    for i in range(m):
        for j in range(c[i], n+1):
            ways[j] += ways[j - c[i]]
    print(ways)
    return ways[n]

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    c = list(map(int, input().split()))
    res = getWays(n, c)
    print(res)
