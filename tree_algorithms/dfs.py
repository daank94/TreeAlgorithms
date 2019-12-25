# Depth-first traversal of nodes in a tree.
from treenode import Node


def preorder(node: Node) -> None:
    if not node:
        return

    print(node.value)
    preorder(node.left)
    preorder(node.right)


def inorder(node: Node) -> None:
    if not node:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)


def postorder(node: Node) -> None:
    if not node:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.value)


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

print("Pre-order traversal:")
preorder(root)

print("In-order traversal:")
inorder(root)

print("Post-order traversal:")
postorder(root)
