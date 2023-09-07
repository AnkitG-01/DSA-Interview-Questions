'''
Largest Subarray with 0 Sum:

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:
Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n,
where n is the size of the array A and returns the length of the largest subarray with 0 sum.

'''
class Solution:
    def maxLen(self, n, arr):
        res=0 #calculating the max length of the 0 sum subarray
        sum=0 #calculate sum of a subarray
        dic={}
        for i in range(n):
            sum+=arr[i]

            if sum==0:
                res=i+1 #if sum of the list iterations is zero, the iterated items form a 0 sum subarray s0 we add the index number+1
            
            if sum in dic:
                res=max(res,i-dic[sum]) #if the current sum is already in dictionary, we set res as max of previous res value or length of 0 sum subarray(i-dic[sum])
            
            else:   
                dic[sum]=i #if sum is not present in dictionary, add it

        return res
s=Solution()
print(s.maxLen(6,[2,-5,3,1,-1,9]))