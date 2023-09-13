def subsetSum(num):
    n=len(num)
    res=[]
    def subset(idx,summ): #helper function
        if idx==n:
            res.append(summ)
            return
        subset(idx+1,summ+num[idx]) #we choose to add the current element to the sum
        subset(idx+1,summ) #we choose to not add the current element to the sum
    subset(0,0)
    res.sort()
    return res