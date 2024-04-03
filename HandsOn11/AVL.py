class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initial height of a new node is 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self._insert_recursively(root.left, key)
        else:
            root.right = self._insert_recursively(root.right, key)

        # Update height of the current node
        self._update_height(root)

        # Perform rotations if necessary to maintain balance
        balance = self._balance_factor(root)

        # Left Left case
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        # Right Right case
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        # Left Right case
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Left case
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    # Additional methods for deletion, searching, traversal, etc.
  
