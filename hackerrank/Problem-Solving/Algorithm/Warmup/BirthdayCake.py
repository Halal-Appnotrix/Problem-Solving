'''
    Problem Link:-https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''
def birthdayCakeCandles(ar):
    maximum_num = max(ar) 
    return ar.count(maximum_num)

if __name__ == "__name__":
    ar = list(map(int, input().split(()))
    res = birthdayCakeCandles(ar)
    print(res)s
