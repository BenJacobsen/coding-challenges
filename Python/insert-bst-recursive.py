# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def recurse(root: TreeNode, val: int):
    if val > root.val:
        if root.right == None:
           root.right = TreeNode(val)
        else:
            recurse(root.right, val)
    elif val < root.val:
        if root.left == None:
           root.left = TreeNode(val)
        else:
            recurse(root.left, val)
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        recurse(root, val)
        return root
    
