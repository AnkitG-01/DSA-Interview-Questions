'''
Mersenne Prime:

Mersenne Prime is a prime number that is one less than a power of two. In other words, any prime is Mersenne Prime if it is of the form 2k-1
 where k is an integer greater than or equal to 2. First few Mersenne Primes are 3, 7, 31 and 127.
The task is to find all Mersenne Primes smaller than equal to an input positive integer n.

'''
class Solution:
    def isPrime(self,n):
        if n<=1:
            return False
        if n%2==0:
            return n==2
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False
        return True
    def AllMersennePrimeNo(self, n):
        k=1
        res=[]
        while 2**k-1<=n:
            p=2**k-1
            if self.isPrime(p):
                res.append(p)
            k+=1
        return res

s=Solution()
print(s.AllMersennePrimeNo(10))