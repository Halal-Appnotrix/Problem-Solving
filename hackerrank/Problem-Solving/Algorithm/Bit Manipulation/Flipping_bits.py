class Solution(object):
    def flippingBits(n):
        n = ~n # Bitwise negation. 
        return (2**32) + n

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = Solution.flippingBits(n)

        print(str(result) + '\n')
