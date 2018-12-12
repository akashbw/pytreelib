from queue import Queue

from .node import BinaryTreeNode

class BinarySearchTree(object):
    """
    Defines a Binary Search Tree.

    Create BST with either of the following constructor:
        - BinarySearchTree()
            -> with no parameter
        - BinarySearchTree(10)
            -> with int as parameter
        - BinarySearchTree(BinaryTreeNode(10))
            -> with BinaryTreeNode as parameter
        - BinarySearchTree([10, 14, 6, 19, 8])
            -> with list of int objects as parameter
    """
    def __init__(self, element=None):
        if isinstance(element, BinaryTreeNode) or (element is None):
            self.root = element
        elif isinstance(element, int):
            self.root = BinaryTreeNode(element)
        elif isinstance(
            element, list) and all(isinstance(x, int) for x in element):
            self.root = BinaryTreeNode(element[0])
            for e in element[1:]:
                self.insert(e)
        else:
            raise TypeError(
            "Supports following types: None, int, list of ints and " + str(
                BinaryTreeNode))

    def _insert_to_left(self, node, parent):
        parent.left = node
        node.parent = parent

    def _insert_to_right(self, node, parent):
        parent.right = node
        node.parent = parent

    def _insert_node(self, node, parent):
        if parent.value == node.value:
            print("Node already exists!")
            # delete node if already present in the tree.
            return
        if parent.value > node.value:
            if not parent.left:
                self._insert_to_left(node, parent)
            else:
                self._insert_node(node, parent.left)
        else:
            if not parent.right:
                self._insert_to_right(node, parent)
            else:
                self._insert_node(node, parent.right)

    def _delink_from_parent(self, node):
        if node.parent:
            if node.is_left_child:
                node.parent.left = None
            elif node.is_right_child:
                node.parent.right = None
            node.parent = None

    def _get_smallest_node(self, starting_node):
        node = starting_node
        while node.left:
            node = node.left
        return node

    def insert(self, value):
        """Creates BinaryTreeNode and inserts in the tree."""
        if not self.root:
            self.root = BinaryTreeNode(value)
            return
        self._insert_node(BinaryTreeNode(value), self.root)

    def _delete_node(self, node):
        if (not node.left) and (not node.right):
            replacement_node = None
        elif node.right:
            replacement_node = self._get_smallest_node(node.right)
        else:
            replacement_node = node.left
        if replacement_node:
            self._delink_from_parent(replacement_node)
            # setting child of node's parent equal to replacement node
            if node.parent:
                if node.is_left_child:
                    node.parent.left = replacement_node
                elif node.is_right_child:
                    node.parent.right = replacement_node
            # setting parent of replacement_node to the node's parent
            replacement_node.parent = node.parent
            # setting children of replacement_node to node's children
            if node.left and node.left != replacement_node:
                replacement_node.left = node.left
            if node.right and node.right != replacement_node:
                replacement_node.right = node.right
        if node == self.root:
            # updating root if targeted node is root
            self.root = replacement_node
        self._delink_from_parent(node)
        del(node)  # deleting the node

    def delete(self, value):
        """Finds node with given value and deletes it from tree."""
        target_node = self.search(value)
        if not target_node:
            return
        self._delete_node(target_node)

    def search(self, value):
        """Find node with given value in the tree."""
        node = self.root
        while node:
            if node.value == value:
                return node
            if value < node.value:
                node = node.left
            else:
                node = node.right

    def status(self):
        """Returns the list of nodes stored in Tree in BFS order"""
        return self._bfs_traversal()

    def display(self):
        """Prints the status of Tree (with BFS traversal)"""
        print("")
        self._bfs_traversal(display=True)
        print ("")

    def _bfs_traversal(self, display=False):
        tree_status = list()
        if not self.root:
            return
        queue = Queue()
        queue.put(self.root)

        while not queue.empty():
            node = queue.get()
            if display:
                print(" ->", node.value, end=" ")
            tree_status.append(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return tree_status
