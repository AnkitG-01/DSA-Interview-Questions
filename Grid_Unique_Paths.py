'''
Grid Unique Paths:

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

'''
class Solution:
    def uniquePaths(self, m, n,memo={}):
        if m==1 or n==1:
            return 1
        if (m,n) in memo:
            return memo[(m,n)]
        memo[(m,n)]=self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        memo[(n,m)]=memo[(m,n)]
        return memo[(m,n)]
s=Solution()
print(s.uniquePaths(3,7))