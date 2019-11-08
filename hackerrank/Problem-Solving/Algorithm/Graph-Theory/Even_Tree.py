class Node:
    def __init__(self):
        self.parent = None
        self.size = 1

    #Add parent of child node.
    def add_parent(self, parent):
        # "self" contain child object reference.
        #so i assign "parent" node as parent node of child node.
        self.parent = parent

        while parent:
            parent.size += 1
            parent = parent.parent


if __name__ == '__main__':

    t_nodes, t_edges = map(int, input().rstrip().split())

    nodes = [Node() for _ in range(t_nodes+1)]

    for i in range(t_edges):
        t_from, t_to = map(int, input().rstrip().split())
        nodes[t_from].add_parent(nodes[t_to])

    res = sum(1 for node in nodes[1:] if node.size % 2 == 0 and node.parent is not None)

    print(str(res) + '\n')
