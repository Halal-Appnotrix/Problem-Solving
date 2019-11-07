class Solution(object):
    def twoArrays(k, A, B):
        A, B = sorted(A), sorted(B, reverse = True)
        for a, b in zip(A, B):
            if a+b < k:
                return "NO"
        return "YES"
            

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = Solution.twoArrays(k, A, B)

        print(result)
