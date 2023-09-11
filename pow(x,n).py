'''
Pow(x,n):

Implement pow(x, n), which calculates x raised to the power n (i.e., x**n).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''
class Solution(object):
    def exp(self,x,n):
        if n==0: #base case
            return 1
        if x==0:
            return 0
        ans=self.exp(x*x,n//2) #binary exponential
        return x*ans if n%2 else ans
    def myPow(self, x, n):
        a=self.exp(x,abs(n))
        return a if n>0 else 1/a