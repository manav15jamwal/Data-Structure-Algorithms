# Approach : Do not go for loops, stick with recursion because tree structure is suitable
#     return max depth out of child subtrees + 1 

class Tree():
    def __init__(self,value=0,left=None,right=None):
        self.value = value
        self.left = left 
        self. right = right
node1 = Tree(4)
node1.left,node1.right = Tree(5),Tree(6)

def depth_of_binary_tree(tree=Tree(),count = 0):
    if tree == None:
        return 0
    return max(depth_of_binary_tree(tree.left),depth_of_binary_tree(tree.right))+1

print(depth_of_binary_tree(node1))