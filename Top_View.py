# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
class Solution:
    def topView(self,root):
        queue=[]
        dic={}
        res=[]
        queue.append([root,0])
        while queue:
            top=queue.pop(0)
            node=top[0]
            col=top[1]
            if col not in dic:
                dic[col]=node.data
            if node.left:
                queue.append([node.left,col-1])
            if node.right:
                queue.append([node.right,col+1])
            
        sorted_col=sorted(dic.keys())
        for col in sorted_col:
            res.append(dic[col])
        return res