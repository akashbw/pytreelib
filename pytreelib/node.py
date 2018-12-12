class BinaryTreeNode(object):
    """
    A BinaryTreeNode with following properties:
        - value: int
        - right: association with BinaryTreeNode designating as right child
        - left: association with BinaryTreeNode designating as left child
        - parent: association with BinaryTreeNode designating as parent
    """
    def __init__(self, value):
        if value and type(value) is not int:
            raise TypeError("Excepts int as arg.")
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    @property
    def is_right_child(self):
        """Returns True if this node is right child of its parent."""
        return self.parent and self == self.parent.right

    @property
    def is_left_child(self):
        """Returns True if this node is left child of its parent."""
        return self.parent and self == self.parent.left

    def __str__(self):
        return "BinaryTreeNode<"+str(self.value)+">"
