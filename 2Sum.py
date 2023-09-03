'''
2 SUM:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

'''
class Solution:
    def twoSum(self, nums, target):
        dicc={}
        for i in range(len(nums)):
            diff=target-nums[i] #calculate diff between target and the list iteration
            if diff in dicc:
                return [i,dicc[diff]] #if the diff is found in the dictionary return the two numbers as list
            dicc[nums[i]]=i #if not found in dictionary then add it to the dictionary
s=Solution()
print(s.twoSum([5,3,6,8,2],9))