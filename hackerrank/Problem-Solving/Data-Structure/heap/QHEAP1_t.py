"""
    It can't pass all test case.
"""
class Solve:
    def __init__(self):
        self.stack = []

    def heap1(self):
        test = int(input())
        for _ in range(test):
            query = input()

            if int(query[0]) is 1:
                q, item = map(int, query.split())
                if self.stack:
                    if self.stack[-1] < item:
                        self.stack[-1], item = item, self.stack[-1]
                        self.stack.append(item)
                    else:
                        self.stack.append(item)
                else:
                    self.stack.append(item)
            elif int(query[0]) is 2:
                q, item = map(int, query.split())
                index_of_item = self.stack.index(item)
                self.stack.pop(index_of_item)
            elif int(query[0]) is 3:
                print(self.stack[-1])

if __name__ == "__main__":
    solve = Solve()
    solve.heap1()
