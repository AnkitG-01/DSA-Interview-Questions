'''
Sqrt(x)

Given an integer A.
Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.
NOTE: Do not use sort function from standard library. Users are expected to
solve this in O(log(A)) time.

Example Input:
X=11

Example Output:
3

'''
def mySqrt(x):
        if x==0:
            return x
        #we are using binary search to find the square root of the given number
        low,high=1,x
        while low<=high:
            mid=(low+high)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                high=mid-1
            else:
                low=mid+1
        return high
print(mySqrt(11))
print(11**0.5)