'''
Reverse Pairs:

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 
Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
'''
class Solution:
    def merge(self,nums,start,mid,end): #merge function of merge sort
        left,right=start,mid+1
        temp=[]
        while left<=mid and right<=end:
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=end:
            temp.append(nums[right])
            right+=1
        for i in range(start, end + 1):
            nums[i] = temp[i - start]

    def countPairs(self,nums,start,mid,end): #function to count reverse pairs
        count=0
        right=mid+1 #pointer to 2nd half of array
        for i in range(start,mid+1):
            while right<=end and nums[i]>2*nums[right]: #we compare first half of array to second half of array such that nums[i]>2*nums[right]
                right+=1 #if true increment right by 1
            count+=right-(mid+1) #add to count
        return count
    
    def merge_sort(self,nums,start,end): #recursive function of merge sort
        count=0
        if start>=end: return count
        mid=(end+start)//2
        count+=self.merge_sort(nums,start,mid) #add count values from recursive function calls
        count+=self.merge_sort(nums,mid+1,end)
        count+=self.countPairs(nums,start,mid,end) #add count value from current iterations
        self.merge(nums,start,mid,end) #after array is fully divided into individual elements start merging in sorted order
        return count
    
    def reversePairs(self, nums):
        return self.merge_sort(nums,0,len(nums)-1)
s=Solution()
print(s.reversePairs([1,3,2,3,1]))