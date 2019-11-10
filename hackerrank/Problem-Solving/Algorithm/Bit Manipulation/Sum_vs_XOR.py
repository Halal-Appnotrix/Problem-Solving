# Complete the sumXor function below.

# It's not able pass all test case.
#class Solution(object):
#    def sumXor(n):
#        count = 0
#        for i in range(n):
#            if n+i == n^i:
#                count += 1
#        return count



# It's able to pass all test case.
class Solution(object):
    def sumXor(n):
        num_of_zero = (bin(n).count('0')) - 1
        return 2**num_of_zero
    
if __name__ == '__main__':

    n = int(input().strip())

    result = Solution.sumXor(n)

    print(str(result) + '\n')

