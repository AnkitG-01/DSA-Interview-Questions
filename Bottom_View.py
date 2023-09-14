class Solution:
    def bottomView(self, root):
        res=[]
        queue=[] #queue to store tuples of node and horizontal distance
        hd_dict={} #hashmap to store nodes at their horizontal distance
        queue.append((root,0)) #add root node to queue
        
        while queue: #while queue is not empty
            node,hd=queue.pop(0) #pop first node of queue
            hd_dict[hd]=node.data #add that node to the dictionary
            if node.left: #if left node is present
                queue.append((node.left,hd-1)) #add node to queue with it's hd
            if node.right: #if right node is present
                queue.append((node.right,hd+1)) #add node to queue with it's hd
        
        sorted_hd=sorted(hd_dict.keys()) #sort the horizontal distances
        
        for hd in sorted_hd:
            res.append(hd_dict[hd]) #add the bottom nodes to res
        
        return res