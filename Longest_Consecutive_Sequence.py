'''
Longest Consecutive Sequence:

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.

'''
class Solution:
    def longestConsecutive(self, nums):
        
        if not len(nums):
            return 0
        
        numSet=set(nums) #use set of list nums for O(1) lookup time
        seq=0 #calculate length of current sequence
        maxseq=1 #find length of longest sequence

        for i in numSet: #iterating through the set
            #if current element's previous number is in the set then its part of an existing set
            if i-1 not in numSet: #if current element's previous number is not in the set then its the starting of a new sequence
                seq=1 #starting length of sequence

                while i+seq in numSet: #if next value of current element present in list
                    seq+=1 #increment sequence length by 1
                
                maxseq=max(maxseq,seq) #set value of max sequence

        return maxseq

s=Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1,10]))