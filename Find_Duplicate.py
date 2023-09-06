'''
Find the Duplicate number:

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

'''
class Solution(object):
    def findDuplicate(self, nums):
        dic={}
        for i in nums: #adding all elements to a hashmap
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i,j in dic.items(): 
            if j>1:
                return i #return the element whose freq is greater than 1