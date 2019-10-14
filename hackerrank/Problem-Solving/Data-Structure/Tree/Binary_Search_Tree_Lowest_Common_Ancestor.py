#Create Node
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

#Binary search Tree
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


#Lowest Common Ancester function.
def lca(root, v1, v2):
  #Enter your code here
  if v1 > v2:
      v1, v2 = v2, v1

  Ancestor = None
  curr_node = root

  while curr_node:
        Ancestor = curr_node

        if v1 <= curr_node.info <= v2:
            return Ancestor
        elif curr_node.info < v1 or curr_node.info < v2:
            curr_node = curr_node.right
        else:
            curr_node = curr_node.left

            
if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    v = list(map(int, input().split()))

    ans = lca(tree.root, v[0], v[1])
    print (ans.info)
