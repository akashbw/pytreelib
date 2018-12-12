pytreelib: Simple Binary Search Tree implementation
===================================================

Description
-----------

This package provides classes that implements Tree data structure and it's variants. 

``BinaryTreeNode`` contains a data element ``value`` and references for ``parent``, ``right`` and ``left`` child.

``BinarySearchTree`` implements a Binary Search Tree data structure. Offers basic functions (``insert, delete, search, status, display``).


Examples
--------
To create a node:

>>> from pytreelib import BinaryTreeNode 
>>> node = BinaryTreeNode(10)           
>>> print(node.value)  # 10            

We can create BST in following ways:

an empty tree:

>>> from pytreelib import BinarySearchTree
>>> tree = BinarySearchTree() 

with only root defined:

>>> from pytreelib import BinaryTreeNode, BinarySearchTree
>>> tree = BinarySearchTree(10)                  
>>> tree = BinarySearchTree(BinaryTreeNode(10))  

with list of ints

>>> from pytreelib import BinarySearchTree
>>> tree = BinarySearchTree([10, 9, 8])         
>>> print(tree.root)  # BinaryTreeNode:10      
>>> print(tree.root.left)  # BinaryTreeNode:8 
>>> print(tree.root.right)  # BinaryTreeNode:9  


Installation
------------

Currently it runs only with python3. Install this package via `pip3`.

``$ pip3 install pytreelib``



