'''
Print all prime factors of a given number

'''
def checkPrime(n):
    if n<=1:
        return False
    if n%2==0:
        return n==2
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
def countPrimes(n):
    res=[]
    for i in range(2,n//2+1):
        if n%i==0 and checkPrime(i):
            res.append(i)
    return res
print(countPrimes(35))