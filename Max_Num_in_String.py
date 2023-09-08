'''
Mystical String of Numeria:

Write a python code that takes a single line containing a string with a mix of letters and numbers as input 
and gives a single integer representing the sum of the merged numbers in the input string as output

Example 1:

Input: 123xyz
Output: 123
Explanation:
The merged number is 123, resulting in a sum of 123.

Example 2:
Input: 1xyz23
Output: 24
Explanation: 
The merged numbers are 1 and 23, resulting in a sum of 24.

'''
class Solution:
    #checks if given character is digit
    def isDigit(self,c):
        return '0'<=c<='9'
    
    def Numeria(self,st):
        total=0 #total of all numbers in the string
        current_num=0 #the number currently being used
        in_Number=False #check if the current string is part of a number 
        #iterating through each character of string
        for i in st:
            #if character i is digit
            if self.isDigit(i):
                in_Number=True
                current_num=current_num*10+int(i)

            else:
                total+=current_num
                in_Number=False
                current_num=0

        if in_Number: #if last character of string was also part of a number
            total+=current_num #add that last number to the total

        return total
s=Solution()
print(s.Numeria("1xyz23"))