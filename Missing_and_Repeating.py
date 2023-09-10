'''
Find the Missing and Repeating Numbers:

You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing.
The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

Example 1:
Input Format:  array[] = {3,1,2,5,3}
Result: {3,4}
Explanation: A = 3 , B = 4 
Since 3 is appearing twice and 4 is missing

Example 2:
Input Format: array[] = {3,1,2,5,4,6,7,5}
Result: {5,8}
Explanation: A = 5 , B = 8 
Since 5 is appearing twice and 8 is missing

'''
def missingAndRepeating(arr, n):
    hmp=[0]*(n+1) #array of n+1 length
    missing=-1 #variable to store missing number
    repeating=-1 #variable to store repeating number

    for i in range(n):
        hmp[arr[i]]+=1 #add frequency of each element in arr

    for i in range(1,n+1):

        if hmp[i]==2: #if any element is occuring twice, then its the repeating element
            repeating=i

        elif hmp[i]==0: #if an element is not occuring, then its missing
            missing=i

        if missing!=-1 and repeating!=-1:
            return [missing,repeating]