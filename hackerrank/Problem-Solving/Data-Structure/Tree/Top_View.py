#Comlixity is O(n) of The topView() function.

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


#Top View function.
def topView(root):
    topValues, node, level = {}, [], 0
    root.level = 0
    node.append(root)

    while(len(node)):
        root, level = node[0], node[0].level

        if level not in topValues:
            topValues[level] = root.info

        if root.left:
            root.left.level = level - 1
            node.append(root.left)
        if root.right:
            root.right.level = level + 1
            node.append(root.right)
        node.pop(0)
    for key in sorted(topValues):
        print(topValues[key], end=' ')


if __name__ == "__main__":
    
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    topView(tree.root)
