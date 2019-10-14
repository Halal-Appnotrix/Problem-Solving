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


def height(root):
    if root is None:
        return 0
    else:
        left = height(root.left)
        right = height(root.right)

        if left > right:
            tree_height = left + 1
        else:
            tree_height = right + 1
    return tree_height

def printTree(root, level):
    if root is None:
        return
    
    if level == 1:
        print(root, end=' ')
    elif level > 1:
        printTree(root.left, level-1)
        printTree(root.right, level-1)

def levelOrder(root):
    #Write your code here
    h = height(root)
    for level in range(1, h+1):
        printTree(root, level)
    

if __name__ == '__main__':

    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    levelOrder(tree.root)
