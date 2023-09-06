'''
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.

'''
class Solution:
    def maxSubArraySum(self,arr,N):
        sum=0 #calculate sum of subarray
        max=float('-inf') #min value to calculate the max sum
        for i in range(N):
            
            sum+=arr[i]
            
            if sum>max:
                max=sum #if sum greater than max, max equals sum
            
            if sum<0:
                sum=0 #if the sum is less than zero it will not contribute to increase the maxSum of the subarray

        return max
s=Solution()
print(s.maxSubArraySum([1,2,3,-2,5],5))     
