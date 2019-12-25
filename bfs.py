# Breadth-first traversal of nodes in a tree.
from treenode import Node


def bfs(node: Node) -> None:
    queue = [node]

    while queue:
        top_node = queue.pop(0)  # Pop the first element (as we will use the array as a queue)

        if top_node:
            print(top_node.value)
            queue.append(top_node.left)
            queue.append(top_node.right)


'''
Create nodes with structure:
       1
  2         3
4   5     6   7
'''
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

bfs(root)
