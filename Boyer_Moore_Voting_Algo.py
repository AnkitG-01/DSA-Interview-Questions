'''
Majority Element:

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
class algo:
    def major(self,arr):
        count,candidate=0,0
        for i in arr:

            if count==0: 
                candidate=i #if value of count is 0 we set the current element as candidate

            if i==candidate:
                count+=1 #if current element is same as candidate, increment count by 1

            else:
                count-=1 #if current element not same as candidate, decrement count by 1
                
        return candidate
al=algo()
print("Majority Element =",al.major([2,2,1,1,1,2,2]))