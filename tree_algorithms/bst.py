# Algorithms related to binary search trees (BSTs).
from treenode import Node


# Check if the given binary search tree contains a node with the given value.
# If so, return that node. Else, return None.
def contains(node: Node, value):
    if not node:
        return None

    if node.value == value:
        return node
    elif value < node.value:
        return contains(node.left, value)
    else:
        return contains(node.right, value)


# Check if the given tree is a binary search tree.
def is_bst(node: Node) -> bool:
    return __is_bst_recur(node, None, None)


def __is_bst_recur(node: Node, smallest_value_allowed, largest_value_allowed) -> bool:
    if not node:
        return True

    if smallest_value_allowed and node.value < smallest_value_allowed:
        return False
    if largest_value_allowed and node.value > largest_value_allowed:
        return False

    return __is_bst_recur(node.left,
                          smallest_value_allowed,
                          min(largest_value_allowed, node.value) if largest_value_allowed else node.value) \
           and __is_bst_recur(node.right,
                              max(smallest_value_allowed, node.value) if smallest_value_allowed else node.value,
                              largest_value_allowed)


# Insert value in the binary search tree.
# Returns new (or existing) node containing the given value in the BST.
def insert(node: Node, value):
    if not node:
        return Node(value)

    return __insert_recur(node, value)


def __insert_recur(node: Node, value):
    if value == node.value:
        return node
    elif value < node.value:
        if node.left:
            insert(node.left, value)
        else:
            node.left = Node(value)
            node.left.parent = node
            return node.left
    else:
        if node.right:
            insert(node.right, value)
        else:
            node.right = Node(value)
            node.right.parent = node
            return node.right


'''
Create nodes with structure:
       6
  3         8
1   4     7   9
'''
root = Node(6)
insert(root, 3)
insert(root, 1)
insert(root, 4)
insert(root, 8)
insert(root, 7)
insert(root, 9)

node9 = contains(root, 9)
print(node9)
print(node9.parent)
print(is_bst(root))

insert(root, 11)
insert(root, 0)
print(root)
