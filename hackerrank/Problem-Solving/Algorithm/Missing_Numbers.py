#This code is able to pass all test case.

class Solve:
    def missingNumbers(self, arr, brr):
        d = {}
        for num in arr+brr:
            d[num] = 0

        for num in arr:
            d[num] += 1
        for num in brr:
            d[num] -= 1
        numbers = sorted([key for key in d.keys() if d[key] != 0])
        
        return numbers

if __name__ == '__main__':
    solve = Solve()

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = solve.missingNumbers(arr, brr)

    print(' '.join(map(str, result)))
