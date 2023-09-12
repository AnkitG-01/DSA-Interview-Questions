'''
Rotate Matrix: 

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
Example 1:

Input:

[[1,2,3],
[4,5,6],
[7,8,9]]

Output:

[[7,4,1],
[8,5,2],
[9,6,3]]

'''
class Solution(object):
    def rotate(self, matrix):
        row=len(matrix) #number of rows
        col=len(matrix[0]) #number of columns
        for i in range(row):
            for j in range(i,col):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j] #transposing the matrix
        for i in range(row):
                matrix[i]=matrix[i][::-1] #reversing the rows
s=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)
print(matrix)
        
        

        
        
