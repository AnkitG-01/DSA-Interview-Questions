'''
Reverse Words in a String:

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

'''
class Solution:
    def reverseWords(self, s):
        res = [] #list to store words
        temp = "" #temporary string
        
        for c in s: #iterating through the string
            
            if c != " ": #if current character is not space then
                temp += c #add character to temp
            
            elif temp != "": #if current character is space and temp is not empty
                res.append(temp) #add the word to res list
                temp = "" #empty temp
        
        if temp!="": #after finishing the loop, if temp not empty
            res.append(temp) #add the last word to res
            temp="" #empty temp
        
        for i in range(len(res)-1,-1,-1):
            
            if i!=0:
                temp+=res[i]+" " #add the words in reverse order seperated by space
            
            else:
                temp+=res[i] #if it's the last word, don't add space

        return temp
s=Solution()
print(s.reverseWords("  a good   example  "))