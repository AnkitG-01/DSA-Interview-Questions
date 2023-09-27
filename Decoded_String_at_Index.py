'''
Decoded String at Index

You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".

Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".

'''
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0
        
        # Calculate the total length of the decoded string
        for c in s:
            if c.isdigit():
                # If the character is a digit, adjust the total length
                # by multiplying it with the numeric value.
                total_length *= int(c)
            else:
                # If the character is an alphabet character, simply increment
                # the total length by 1 to account for the character itself.
                total_length += 1
        
        # Traverse the string in reverse to find the character at position k
        for c in reversed(s):
            k %= total_length  # Reduce k based on the current total length
            
            if k == 0 and c.isalpha():
                # If k becomes 0, and the current character is an alphabet character,
                # it means we've reached the desired position k, so return this character.
                return c
            
            if c.isdigit():
                # If the character is a digit, adjust the total length by dividing it
                # by the numeric value. This effectively "undo" the repetition of characters.
                total_length //= int(c)
            else:
                # If the character is an alphabet character, decrement the total length
                # by 1 to account for this character.
                total_length -= 1
        
        return ""  # This line should not be reached, but added for completeness