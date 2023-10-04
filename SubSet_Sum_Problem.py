'''
Subset Sum

Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 30
Output: 0
Explanation: There is no subset with sum 30.

'''
class Solution:
    
    def isSubsetSum (self, N, arr, sum):
        dp=[[-1 for i in range(sum+1)] for j in range(N+1)]
        def helper(N,arr,sum):
            if sum==0:
                return 1
            if N<=0:
                return 0
            if dp[N][sum] != -1:
                return dp[N][sum]
            if arr[N-1]>sum:
                dp[N-1][sum]=helper(N-1,arr,sum)
                return dp[N-1][sum]
            else:
                dp[N-1][sum]=helper(N-1,arr,sum)
                return dp[N-1][sum] or helper(N-1,arr,sum-arr[N-1])
        return helper(N,arr,sum)    
        
s=Solution()
l=[3,4,12,32,5]
target=6
print(s.isSubsetSum(len(l),l,target))
