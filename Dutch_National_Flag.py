'''
Sort Colors:

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

'''
class Solution(object):
    def sortColors(self, nums):
        low,mid,high=0,0,len(nums)-1 #take 3 pointers low,mid and high
        #our goal is to make sure all elements before the low pointer are 0, all elements after the high pointer are 2 and the elements between low and high are 1 
        while mid<=high:

            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low] #swap the numbers at mid and low if nums[mid]=0
                low+=1 
                mid+=1
                #increment low and mid to cover the rest of the list
            elif nums[mid]==1:
                mid+=1 #if mid points to 1 increment mid

            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1 #if mid points to 2, swap numbers at mid and high and decrement high 
s=Solution()
colors=[0,2,1,2,1,0,1,0]
s.sortColors(colors)
print(colors)