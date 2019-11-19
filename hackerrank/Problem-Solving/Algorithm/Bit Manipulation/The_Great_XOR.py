def theGreatXor(x):
    
    return (1 << x.bit_length()) - x - 1)

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = theGreatXor(x)

        print(str(result) + '\n)
