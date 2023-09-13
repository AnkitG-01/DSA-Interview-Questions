'''
Count Primes:

Given an integer n, return the number of prime numbers that are strictly less than n.

'''
class Solution:
    def countPrimes(self, n):
        if n == 0 or n == 1: 
                return 0
        arr = [True] * n #first we create a boolean array of size n

        arr[0], arr[1] = False, False #set 0 and 1 indices as False as they are not prime no 

        for i in range(2, int(n ** 0.5) + 1): #run for loop from 2 to square root of n
                if arr[i]: #if value of index i is True then
                        for j in range(i * i, n, i): #run for loop from i*i to n and set the j indices as false 
                                arr[j] = False

        return sum(arr)  #sums all the numbers in the list
s=Solution()
print(s.countPrimes(100))