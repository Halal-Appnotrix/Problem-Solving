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


def findHeight(root):
    if root is None:return 0
    
    left = findHeight(root.left)
    right = findHeight(root.right)
    if left > right:
        tree_height = 1 + left
    else:
        tree_height = 1 + right
    
    return tree_height

def height(root):
    if root is None:return 0
    else:
        tree_height = findHeight(root)
        return tree_height - 1


if __name__=="__main__":
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))