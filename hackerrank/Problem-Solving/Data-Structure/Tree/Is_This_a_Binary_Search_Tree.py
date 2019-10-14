'''
    Problem Link:-https://www.hackerrank.com/challenges/is-binary-search-tree/problem

    Coplixity:-
	Wrost Case:-O(n+n)->
        averege Case:-O(n+n/2)
        Best Case:-O(n+1)
'''

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def inOrderTree(root, list_):
    if root.left:
        inOrderTree(root.left, list_)
    list_.append(root.data)
    if root.right:
        inOrderTree(root.right, list_)
    
def check_binary_search_tree_(root):
    list_ = []
    inOrderTree(root, list_)
    length = len(list_)
    for i in range(1, length):
        if list_[i-1] >= list_[i]:
            return False
    return True
