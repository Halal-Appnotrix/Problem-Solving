'''
    Problem Link:-https://www.hackerrank.com/challenges/find-the-running-median/problem
    
'''

import bisect

def runningMedian(a):
    res = []
    list_ = []
    
    for item in a:
        bisect.insort(list_, item)
        length_list_ = len(list_)
        mid = length_list_ // 2
        if length_list_ % 2 == 1:
            res.append(float(list_[mid]))
        else:
            sum_ = list_[mid-1] + list_[mid]
            div = sum_ / 2
            res.append(div)
    return res

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res = runningMedian(a)
    print("\n".join(str(item) for item in res))
