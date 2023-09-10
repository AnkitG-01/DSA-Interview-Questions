'''
Problem Description

Given a string A. The only operation allowed is to insert characters at the beginning of the string.
Find how many minimum characters are needed to be inserted to make the string a palindrome string.

Input Format
The only argument given is string A.


Output Format
Return the minimum characters that are needed to be inserted to make the string a palindrome string.


Example 1:

Input 1: A = "ABC"
Output 1: 2
Explanation 1:
Insert 'B' at beginning, string becomes: "BABC".
Insert 'C' at beginning, string becomes: "CBABC".

Example 2:

Input 2: A = "AACECAAAA"
Output 2: 2
Explanation 2:
Insert 'A' at beginning, string becomes: "AAACECAAAA".
Insert 'A' at beginning, string becomes: "AAAACECAAAA".

'''
def minCharsforPalindrome(str):
    i,j,trim=0,len(str)-1,len(str)-1
    count=0
    while i<j:
        if str[i]==str[j]:
            i+=1
            j-=1
        else:
            count+=1
            i=0
            trim-=1
            j=trim
    return count
print(minCharsforPalindrome("ABCD"))