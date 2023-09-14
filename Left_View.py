class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    res=[]
    def left(root,depth):
        if not root:
            return
        if depth==len(res):
            res.append(root.data)
        left(root.left,depth+1)
        left(root.right,depth+1)
    left(root,0)
    return res