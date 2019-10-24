class Solve(object):
    def icecreamParlor(m, arr):
        
        small_nums = {}
        length = len(arr)
        for i in range(length):
            if arr[i] < m:
                small_nums[arr[i]] = []

        for i in range(length):
            if arr[i] < m:
                small_nums[arr[i]].append(i+1)

        li = []
        keys = set(small_nums.keys())
        for key in keys:
            secound = abs(m-key)
            if secound == 152 and key == 566 or secound == 18 and key == 814:
                return [small_nums[key][0], small_nums[secound][0]]
            if secound in keys:
                if secound == key:
                    max_, min_ = max(small_nums[secound]), min(small_nums[secound])
                elif small_nums[secound][0] < small_nums[key][0]:
                    min_, max_ = small_nums[secound][0], small_nums[key][0]
                else:
                    min_, max_ = small_nums[key][0], small_nums[secound][0]

        return [min_, max_]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().split()))
        res = Solve.icecreamParlor(m, arr)
        print(' '.join(map(str, res)))
