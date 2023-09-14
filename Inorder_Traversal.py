class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        ans=[]
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans