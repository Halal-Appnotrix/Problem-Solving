'''
    Problem Link:-https://www.hackerrank.com/challenges/diagonal-difference/problem
'''

def diagonalDifference(arr):
    # Write your code here
    sum1, sum2 = 0, 0
    length = len(arr)
    for i in range(length):
        sum1 += arr[i][i]
        sum2 += arr[i][length-1-i]
    return abs(sum1 - sum2)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = diagonalDifference(arr)
    print(res)
