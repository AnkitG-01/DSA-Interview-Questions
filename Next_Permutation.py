'''
Next Permutation:

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

'''
class Solution(object):
    def nextPermutation(self, nums):

        n=len(nums)
        bp=-1 #the breakpoint variable will find the element which is smaller than the next element in the list when iterated from reverse

        #Step 1: Find the breakpoint
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]: 
                bp=i #if an element is found that is smaller than the next element we take its index in bp and break loop
                break

        if bp==-1: #if breakpoint doesn't exist
            nums[:]=nums[::-1] #just reverse the array
            return
        
        #Step 2: Find the next Greatest Element and swap it with the breakpoint element
        for j in range(n-1,bp,-1):
            if nums[j]>nums[bp]:
                nums[j],nums[bp]=nums[bp],nums[j]
                break
        
        #Step 3: Reverse the right half
        nums[bp+1:]=nums[-1:bp:-1] 
        return
    
s=Solution()
A=[1,3,2]
s.nextPermutation(A)
print(A)