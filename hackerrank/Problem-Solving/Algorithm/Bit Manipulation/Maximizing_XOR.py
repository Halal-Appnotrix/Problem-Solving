from itertools import combinations_with_replacement


def maximizingXor(l, r):
    li = list(range(l, r+1))
    max_ = 0
    permuts = combinations_with_replacement(li, 2)
    for permut in permuts:
        XOR = (permut[0] ^ permut[1])
        max_ = max(XOR, max_)

    return max_

if __name__ == '__main__':

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    print(str(result) + '\n')
