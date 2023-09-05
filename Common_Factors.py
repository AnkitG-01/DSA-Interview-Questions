'''
Find no of common factors

'''
class Solution:
    def gcd(self,a,b):
        if a==0:
            return b
        return self.gcd(b%a,a)
    def commDiv (self, a, b):
        count=0
        hcf=self.gcd(a,b) #calculate gcd using euclidean algorithm
        for i in range(1,int(hcf**0.5)+1):
            if hcf%i==0:
                count+=2 #increment count by 2 as both a and b are divisible by the divisor
            if i*i==hcf:
                count-=1 #if hcf has a perfect sq root then decrement count by 1 as it would've been count twice in the previous step 
        return count
S=Solution()
print(S.commDiv(20,36))