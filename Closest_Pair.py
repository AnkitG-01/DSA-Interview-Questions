'''
Find the closest pair from two arrays

Given two sorted arrays arr and brr and a number x, find the pair whose sum is closest to x and the pair has an element from each array. 
In the case of multiple closest pairs return any one of them.

Note: Can return the two numbers in any manner.

Example 1:

Input: N = 4, M = 4
arr[] = {1, 4, 5, 7}
brr[] = {10, 20, 30, 40} 
X = 32

Output: 
1, 30

Explanation:
The closest pair whose sum is closest
to 32 is {1, 30} = 31.

Example 2:

Input: N = 4, M = 4
arr[] = {1, 4, 5, 7}
brr[] = {10, 20, 30, 40}
X = 50 

Output: 
7, 40 

Explanation: 
The closest pair whose sum is closest
to 50 is {7, 40} = 47.

'''
class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        i,j=0,m-1
        res=None
        min=float('inf')
        while i<n and j>=0:
            sum=arr[i]+brr[j]
            diff=abs(x-sum)
            if diff<min:
                min=diff
                res=[arr[i],brr[j]]
            if sum>x:
                j-=1
            elif sum<x:
                i+=1
            else:
                break
        return res