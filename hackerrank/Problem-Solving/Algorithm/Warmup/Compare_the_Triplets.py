'''
    Problem Link:-https://www.hackerrank.com/challenges/compare-the-triplets

'''

def compareTriplets(a, b):
    length = len(a)
    li = [0]*2
    for i in range(length):
        if a[i] > b[i]:
            li[0] += 1
        elif a[i] < b[i]:
            li[1] += 1
        elif a[i] == a[i]:
            continue
    return li

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = compareTriplets(a, b)
    print(res)
