'''
Repeated String Match:

Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. 
If it is impossible for b to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:

Input: a = "a", b = "aa"
Output: 2
 
'''
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        c=1
        n=len(b)
        t=a
        while b!=t and len(t)<=n:
            c+=1
            t=a*c
        if b in t:
            return c
        if b in a*(c+1):
            return c+1
        return -1
            