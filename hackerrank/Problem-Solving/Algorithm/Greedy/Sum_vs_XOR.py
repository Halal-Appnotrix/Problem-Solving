# Complete the sumXor function below.
class Solution(object):
    def sumXor(n):
        count = 0
        for i in range(n):
            if n+i == n^i:
                count += 1
        return count

if __name__ == '__main__':

    n = int(input().strip())

    result = Solution.sumXor(n)

    print(str(result) + '\n')

