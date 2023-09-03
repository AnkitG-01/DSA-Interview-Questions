'''
2Sum II:

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

'''
class Solution:
    def twoSum(self, numbers, target):
        
        p1=0 #first pointer pointing to top element of list
        p2=len(numbers)-1 #second pointer pointing to last element of list
        
        while p1<p2: #base case
            
            diff=target-numbers[p1] #the diff between target and first number
            
            if diff>numbers[p2]:
                p1+=1 #if diff greater than second number then increment the first pointer
            
            elif diff<numbers[p2]:
                p2-=1 #if diff less than second number then decrement the second pointer
            
            else:
                return [p1+1,p2+1] #if diff equals second number return the pointers as list after incrementing by 1 as its a 1-indexed array
s=Solution()
print(s.twoSum([1,4,6,8,11],10))