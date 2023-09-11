'''
Permutations:

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

'''
class Solution:
    #uses backtracking to calculate all the permutations
    def permute(self, nums):
        if len(nums)==1: #base case
            return [nums[:]] #if length of the list is 1, return a copy of that list
        
        res=[] #list to store the permutations

        for i in range(len(nums)):
            a=nums.pop(0) #pop the first element of the list
            
            perms=self.permute(nums) #recursively call the permute function with the list after popping the first element

            for perm in perms:
                perm.append(a) #add the popped element to the end of the permutations

            res.extend(perms) #add all the permutations in perms list to res list
            nums.append(a) #add the popped element back to nums list but at the end to make sure the same element is not popped every time
        return res
s=Solution()
print(s.permute([1,2,3]))