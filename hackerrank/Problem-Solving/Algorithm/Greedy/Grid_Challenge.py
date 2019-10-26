# Complete the gridChallenge function below.
def gridChallenge(grid):
    l = len(grid)
    for i in range(l-1):
        l_inner = len(grid[i])
        for j in range(l_inner-1):
            if (grid[i][j] > grid[i][j+1]) or grid[i][j] > grid[i+1][j]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = sorted(input())
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)
