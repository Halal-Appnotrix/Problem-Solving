'''
    Problem Link:-https://www.hackerrank.com/challenges/mini-max-sum/problem
'''

def miniMaxSum(arr):
    Suming_arr = [ sum(arr) - i for i in arr ]
    print(min(Suming_arr), max(Suming_arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

