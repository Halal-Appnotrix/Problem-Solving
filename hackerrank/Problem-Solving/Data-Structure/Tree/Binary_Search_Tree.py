class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None
    
    #Insertion method.
    def insert(self, val):
        #Enter you code here.
        last_node = None
        if self.root is None:
            self.root = Node(val)
        else:
            current_node = self.root
            while current_node is not None:
                last_node = current_node

                if val < current_node.info:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            
            if val < last_node.info:
                last_node.left = Node(val)
            else:
                last_node.right = Node(val)

        return self.root


if __name__ == "__main__":
        
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.insert(arr[i])

    preOrder(tree.root)
