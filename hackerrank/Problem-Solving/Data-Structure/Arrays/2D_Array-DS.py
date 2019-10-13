def hourglassSum(arr):
    add = 0
    sum_list = []
    for i in range(4):
        for j in range(4):
            add = sum(arr[0+i][0+j:3+j])+arr[1+i][1+j]+sum(arr[2+i][0+j:3+j])
            sum_list.append(add)
    return max(sum_list)

if __name__ == "__main__":
    arr = []
    for _ in range(6    ):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
