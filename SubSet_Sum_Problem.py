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
    
    def isSubsetSum(self,N,arr,sum,memo={}):
        if sum==0:
            return True
        if N<=0:
            return False
        if (N,sum) in memo:
            return memo[(N,sum)]
        if arr[N-1]>sum:
            memo[(N-1,sum)] = self.isSubsetSum(N-1,arr,sum)
            return memo[(N-1,sum)]
        else:
            memo[(N-1,sum)] = self.isSubsetSum(N-1,arr,sum)
            memo[(N-1,sum-arr[N-1])] = self.isSubsetSum(N-1,arr,sum-arr[N-1])
            return memo[(N-1,sum)] or memo[(N-1,sum-arr[N-1])]
           
        
s=Solution()
l=list(map(int,input().split()))
target=4877
print(s.isSubsetSum(len(l),l,target))
