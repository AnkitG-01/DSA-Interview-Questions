class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        res=[]
        def right(root,depth):
            if not root:
                return
            if depth==len(res):
                res.append(root.data)
            right(root.right,depth+1)
            right(root.left,depth+1)
        right(root,0)
        return res