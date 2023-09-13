'''
Trapping Rain Water

Given an array arr[] of N non-negative integers representing the height of blocks. 
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 

Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}

Output:
10

Example 2:

Input:
N = 4
arr[] = {7,4,0,9}

Output:
10

Explanation:
Water trapped by above 
block of height 4 is 3 units and above 
block of height 0 is 7 units. So, the 
total unit of water trapped is 10 units.

Example 3:

Input:
N = 3
arr[] = {6,9,9}

Output:
0

Explanation:
No water will be trapped.

'''
class Solution:
    def trap(self, height) -> int:
        n=len(height)
        if n<=2:
            return 0
        res=0
        l=0 #leftmost pointer
        r=n-1 #rightmost pointer
        maxl=height[l] #height at leftmost pointer
        maxr=height[r] #height at rightmost pointer
        while l<r: 
            if maxl<maxr: #if value at left pointer less than value at right pointer #type:ignore
                l+=1 #increment left by 1
                maxl=max(maxl,height[l]) #set maxl as maximum of either previous value or new value
                res+=maxl-height[l] #add the difference to result
            else: #if value at left pointer greater than or equal to right pointer 
                r-=1 #decrement right by 1
                maxr=max(maxr,height[r]) #set maxr as maximum of either new value or previous value
                res+=maxr-height[r] #add difference to result
        return res