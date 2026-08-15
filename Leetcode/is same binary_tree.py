# Goal : To check if binary trees are same , i.e order and values
# Approach : Use a recurrence function which checks similarity of node values , and recurrences until all child nodes are traversed

class Tree():
    def __init__(self,value=0,left=None,right=None):
        self.value = value
        self.left = left 
        self. right = right

def is_same_binary_tree(a=Tree(),b=Tree()):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.value != b.value:
        return False
    return is_same_binary_tree(a.left,b.left) and is_same_binary_tree(a.right,b.right)


node1 = Tree(4)
node1.left,node1.right = Tree(5),Tree(6)
node2 = Tree(4)
node2.left,node2.right = Tree(5),Tree(6)
print(is_same_binary_tree(node1,node2))
node2.right.right = Tree(7)
print(is_same_binary_tree(node1,node2))
