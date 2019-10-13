class Solve:
    def runningTime(self, arr):
        count = 0

        for i in range(1, len(arr)):
            item = arr[i]
            j = i -1

            while j >= 0 and item < arr[j]:
                arr[j+1] = arr[j]
                j = j - 1
                count += 1

            arr[j+1] = item
        return count

if __name__ == "__main__":
    solve = Solve()
    n = int(input())
    arr = list(map(int, input().split()))
    count = solve.runningTime(arr)
    print(count)
