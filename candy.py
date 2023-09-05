'''
Allocate Candy

N children are standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following
requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
What is the minimum number of candies you must give?

Example Input:
arr=[1,2,87,87,87,2,1]

Example Output:
13

'''
def candy(arr):
        res=0
        n=len(arr)
        forward=[0]*n
        backward=[0]*n
        
        for i in range(n):
            forward[i]=1
            if i>0 and arr[i]>arr[i-1]: #if current child's rating is greater than the previous child
                forward[i]=forward[i-1]+1 #current child will get one more candy than previous child
        for i in range(n-1,-1,-1):
            backward[i]=1
            if i<n-1 and arr[i]>arr[i+1]: #if current child's rating is greater than the next child
                backward[i]=backward[i+1]+1 #current child will get one more candy than next child
        for i in range(n):
            res+=max(forward[i],backward[i])
        return res
print(candy([1,2,87,87,87,2,1]))