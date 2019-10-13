'''
    Problem Link:-https://www.hackerrank.com/challenges/recursive-digit-sum/problem

    I can solve this various way or technically.Firstly i use recursive method and also i will show an another sort way.
    you can find out by this statement "print((n*k) % 9 or 9)". 
'''


#Using Recursive method
def findSuperDigit(p):
    int_p = int(p)

    if int_p < 10:
        return int_p
    else:
        sum = 0
        for item in p:
            sum = sum + int(item)
        return findSuperDigit(str(sum))
                       
def superDigit(n, k):
    p = n*k
    res = findSuperDigit(p)
    return res


def tes_superDigit():
    n, k = 12, 2
    assert superDigit(n, k) == 6
                       

if __name__ == "__main__":
    n, k = '2', 2
    res = superDigit(n, k)
    print(res)
