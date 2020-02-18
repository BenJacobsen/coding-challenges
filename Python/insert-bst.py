# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        ins = TreeNode(val)
        cur = top_root = root
        if root == None:
            return ins
        while(True):
            if val > cur.val:
                if cur.right == None:
                    cur.right = ins
                    break
                else:
                    cur = cur.right
            elif val < cur.val:
                if cur.left == None:
                    cur.left = ins
                    break
                else:
                    cur = cur.left
            else:
                break
        return top_root