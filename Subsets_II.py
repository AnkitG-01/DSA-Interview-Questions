'''
Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets.

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

'''
class Solution:
    def subsetsWithDup(self, nums):
        ans = []
        res = set()
        ds = []
        nums.sort() 
        
        def fun(nums, index):
          if index == len(nums):
            res.add(tuple(ds))
            return

          ds.append(nums[index])
          fun(nums, index + 1)
          ds.pop()
          fun(nums, index + 1)

        fun(nums, 0)

        for subset in res:
          ans.append(list(subset))

        return ans

    
