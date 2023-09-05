'''
Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring 
contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

'''
def lookAndSequence(n):
	if n==1: #base case
		return "1"
	
	prev=lookAndSequence(n-1) #previous term
	cnt=1 #count occurence of each digit
	res="" #resulting string at nth term 
	
	for i in range(len(prev)):
		
		if i==len(prev)-1 or prev[i]!=prev[i+1]: #if next digit is not equal to current digit or if its the last digit
			res+=str(cnt)+prev[i] #add the occurence and digit to res
			cnt=1 #reset count to 1
			
		else:
			cnt+=1 #if next digit equal to current digit, increment count by 1
			
	return res
print(lookAndSequence(6))