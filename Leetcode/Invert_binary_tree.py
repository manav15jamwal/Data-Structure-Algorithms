# Goal: To invert binary tree
# Approach: pick a node , swap it with the sibling,
# recurse the function for each and store it
#     and the end return the tree
from Depth_of_binary_tree import Tree,node1

def invert_binary_tree(tree=Tree()):
    if tree == None:
        return None 
    tree.left,tree.right = tree.right,tree.left
    tree.right = invert_binary_tree(tree.right)
    tree.left = invert_binary_tree(tree.left)
    return tree
node1 = invert_binary_tree(node1)
