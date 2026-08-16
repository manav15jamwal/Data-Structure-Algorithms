# Goal : To check if a path exists in a tree which equals to the target sum
# Approach : subtract the value of the node from target sum if it reaches 0 
# return True else recursively check for child nodes

from is_same_binary_tree import Tree,node1

def path_sum(tree=Tree(),target_sum=0):
    if tree is None:
        return False
    target_sum-=tree.value
    if target_sum == 0 and tree.right is None and tree.left is None:
        return True
    return path_sum(tree.left,target_sum) or path_sum(tree.right,target_sum)

print(path_sum(node1,10))