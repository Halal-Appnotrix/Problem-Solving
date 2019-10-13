'''
    Poblem Link:-https://www.hackerrank.com/challenges/the-power-sum/problem

    Look at below, I will try to clear by visualiasion.

            Here, X = 5, N = 2 and also I will use extra paramitter at powerSum() method for find out the distination value.
            Let's strating.........
                        powerSum(5, 2, 1)                   ->1^2
                            /          \
                           /            \
                          /              \
                powerSum(5, 2, 2)      powerSum(4, 2, 2)    ->2^2
                  /          \               |
                 /            \              |
                /              \            (1)
powerSum(5, 2, 3)   powerSum(1, 2,3)                        ->3^2
        |                    |  
        |                    |
       (0)                  (0)
'''

def powerSum(X, N, num):
    power_val = num**N

    if power_val == X:
        return 1

    if power_val > X:
        return 0

    if power_val < X:
        return powerSum(X, N, num+1) + powerSum(X - power_val, N, num+1)


#testing method
def test_powerSum():
    assert powerSum(10, 2, 1) == 1
    assert powerSum(100, 2, 1) == 3
    assert powerSum(100, 3, 1) == 1
