'''
Searching in 2D Array:

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

'''
class Solution:
    def searchMatrix(self, matrix, target):
        #Using Binary Search in 2D Array
        low=0 #starting pointer
        high=len(matrix)*len(matrix[0])-1 #last pointer
        n=len(matrix[0]) #number of columns
        while low<=high:
            mid=(low+high)//2 #calculating middle index
            element=matrix[mid//n][mid%n] #row=mid//n and col=mid%n
            if element<target:
                low=mid+1
            elif element>target:
                high=mid-1
            else:
                return True
        return False
s=Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],5))