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


# Check if the given node is the root for a tree (no cycles)
def is_tree(node: Node) -> bool:
    return __is_tree_recur(node, set())


def __is_tree_recur(node: Node, nodes_visited: set) -> bool:
    if not node:
        return True

    if node in nodes_visited:
        return False
    nodes_visited.add(node)

    return __is_tree_recur(node.left, nodes_visited) and __is_tree_recur(node.right, nodes_visited)


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


# Delete a given node from a binary search tree.
# Return the root of the new binary search tree (will be different to given root if node_to_delete is root node).
def delete(root: Node, node_to_delete: Node) -> Node:
    
    # Special case, node_to_delete is root node
    # Create a dummy node, which we will have to remove later.
    if node_to_delete == root:
        dummy_root = Node(0)
        dummy_root.left = root
        root.parent = dummy_root
    else:
        dummy_root = None

    # Node without children: simply remove the node.
    if not node_to_delete.left and not node_to_delete.right:
        if node_to_delete.parent.left == node_to_delete:
            node_to_delete.parent.left = None
        else:
            node_to_delete.parent.right = None

    # Node with one child: make the parent point to the child.
    elif (not node_to_delete.left) != (not node_to_delete.right):
        child_node = node_to_delete.left or node_to_delete.right

        if node_to_delete.parent.left == node_to_delete:
            node_to_delete.parent.left = child_node
        else:
            node_to_delete.parent.right = child_node

    # Node with two children: get the smallest larger node, replace with the node to delete, then delete the swapped
    # node.
    else:
        node_to_swap = node_to_delete.right
        while node_to_swap.left:
            node_to_swap = node_to_swap.left

        node_to_delete.value = node_to_swap.value
        delete(root, node_to_swap)

    # If the node to delete was the root node, we will have to recover that node.
    if dummy_root:
        root = dummy_root.left

    return root


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
print(is_tree(root))
print(is_bst(root))

print(root)
root = delete(root, contains(root, 6))
print(root)

root2 = Node(5)
insert(root2, 6)
insert(root2, 7)

print(root2)
root2 = delete(root2, contains(root2, 5))
print(root2)
