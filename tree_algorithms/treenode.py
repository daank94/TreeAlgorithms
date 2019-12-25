class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self) -> str:
        return "Node [value: '" + str(self.value) + "', left: " + str(self.left) + ", right: " + str(self.right) + "]"
