'''
Valid Anagrams:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): #if length of two strings are not same definitely not anagram
            return False
        
        hmp_s={} #hashmap to store the occurence of each letter in s
        hmp_t={} #hashmap to store the occurence of each letter in t

        for i in range(len(s)): #storing the occurence of each letter of the strings in hashmaps
            hmp_s[s[i]]=1+hmp_s.get(s[i],0) 
            hmp_t[t[i]]=1+hmp_t.get(t[i],0)

        for key in hmp_s: #iterating through the keys of hashmap of s
            if hmp_s[key]!=hmp_t.get(key,0): #if that key's value is not the same in hashmap of t or if that key is not present
                return False #return false
            
        return True #else return true