def reverseArray(a):
    return a[::-1]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res = reverseArray(a)
    print(res)
