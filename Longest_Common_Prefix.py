'''
Longest Common Prefix:

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
class Solution:
    def longestCommonPrefix(self, strs):
        res="" #string to return result

        for i in range(len(strs[0])):

            for st in strs: #iterating through the list of strings

                if i==len(st) or st[i]!=strs[0][i]: #either if i goes out of bounds of st or st[i] is not common
                    return res #return res
                
            res+=strs[0][i] #add the character to res

        return res