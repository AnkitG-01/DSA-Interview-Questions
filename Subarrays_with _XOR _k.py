'''
Count the number of subarrays with given xor K:

Problem Statement: Given an array of integers A and an integer B. 
Find the total number of subarrays having bitwise XOR of all elements equal to k.

Examples
Example 1:
Input Format: A = [4, 2, 2, 6, 4] , k = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

Example 2:
Input Format: A = [5, 6, 7, 8, 9], k = 5
Result: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]

'''
from collections import defaultdict
def subarraysWithXorK(a, k):
    n = len(a) # size of the given array.
    xr = 0
    mpp = defaultdict(int) # declaring the dictionary.
    mpp[xr] = 1 # setting the value of 0.
    cnt = 0

    for i in range(n):
        # prefix XOR till index i:
        xr = xr ^ a[i]

        # By formula: x = xr^k:
        x = xr ^ k

        # add the occurrence of xr^k
        # to the count:
        cnt += mpp[x]

        # Insert the prefix xor till index i
        # into the dictionary:
        mpp[xr] += 1

    return cnt