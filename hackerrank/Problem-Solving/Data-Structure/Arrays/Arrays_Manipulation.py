from itertools import accumulate

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    n += 1
    li = [0] * n
    for que in queries:
        a, b, k = que
        li[a - 1] += k
        li[b] -= k
    
    return max(accumulate(li))

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')

