class Solve(object):
    def minimumAbsoluteDifference(arr):
        arr = sorted(arr)
        l = len(arr)
        return min([abs(arr[i-1]-arr[i]) for i in range(1, l)])


if __name__=="__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = Solve.minimumAbsoluteDifference(arr)
    print(str(res) + '\n')
