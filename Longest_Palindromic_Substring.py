'''
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

'''
class Solution:
    def checkPalindrome(self,str,left,right): #return palindromic substrings
        
        while left>=0 and right<len(str) and str[left]==str[right]: #checks if characters at left and right pointers are same
            left-=1 #decrement left by 1
            right+=1 #increment right by 1
        
        return str[left+1:right] #returning the palindrome
    
    def longestPalindrome(self,s):
        res="" #string to return longest palindrome

        for i in range(len(s)):
            pal1=self.checkPalindrome(s,i,i) #select all odd palindromes
            
            if len(pal1)>len(res):
                res=pal1 #keep the longest palindrome in res
            
            pal2=self.checkPalindrome(s,i,i+1) #select all even palindromes
            
            if len(pal2)>len(res):
                res=pal2 #keep the longest palindrome in res

        return res
s=Solution()
print(s.longestPalindrome("ababa"))