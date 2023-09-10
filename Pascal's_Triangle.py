'''
Pascal's Triangle:

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''
class Solution(object):
    def generate(self, numRows):
        list=[]
        for i in range(numRows):
            row=[0]*(i+1)
            row[0]=1
            row[i]=1
            for j in range(1,i):
                row[j]=list[i-1][j-1]+list[i-1][j]
            list.append(row)
        return list
s=Solution()
print(s.generate(7))