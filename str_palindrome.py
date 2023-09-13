'''
Check Palindrome:

Given a string, determine if it is a palindrome. While checking for a 
palindrome, you have to ignore spaces, case, and all special characters; i.e. 
consider only alphanumeric characters.

Example Input:
s="A man, a plan, a canal: Panama"

Example Output:
1

'''
def palin(input_str):
    def removeandlower(st):
        new_st=""
        for c in st:
            if 'a'<=c<='z':
                new_st+=c
            if 'A'<=c<='Z':
                new_st+=chr(ord(c)+32)
        return new_st
    st=removeandlower(input_str)
    s=""
    for i in range(len(st)-1,-1,-1):
        s+=st[i]
    if s==st:
        return 1
    else:
        return 0
input_str=input()
print(palin(input_str))
