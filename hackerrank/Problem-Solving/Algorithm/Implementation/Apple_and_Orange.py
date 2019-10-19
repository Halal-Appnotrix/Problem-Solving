# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, m, n, apples, oranges):
    count_a, count_b = 0, 0
    
    for i in range(m):
        if s <= (apples[i]+a) <= t :
            count_a += 1
    for j in range(n):
        if s <= (oranges[j]+b) <= t:
            count_b += 1
    print(count_a)
    print(count_b)


if __name__ == '__main__':
    st = input().split()
    
    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, m, n, apples, oranges)
