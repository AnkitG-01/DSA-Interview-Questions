class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root):
        queue=[]
        dic={}
        res=[]
        queue.append([root,0,0])
        while queue:
            top=queue.pop(0)
            node=top[0]
            col=top[1]
            depth=top[2]
            if col not in dic:
                dic[col]=[(depth,node.val)]
            else:
                dic[col].append((depth,node.val))
            if node.left:
                queue.append([node.left,col-1,depth+1])
            if node.right:
                queue.append([node.right,col+1,depth+1])
        sorted_col=sorted(dic.keys())
        for col in sorted_col:
            values=dic[col]
            values.sort()
            res.append([value for level,value in values])
        return res