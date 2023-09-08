'''
Maximum Product Subarray:

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6

Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''
class Solution:
    def maxProduct(self, nums):
        n=len(nums)
        prefix=suffix=1
        maxP=float('-inf')
        for i in range(n):
            if not prefix:
                prefix=1
            if not suffix:
                suffix=1
            prefix*=nums[i]
            suffix*=nums[n-1-i]
            maxP=max(maxP,prefix,suffix)
        return maxP