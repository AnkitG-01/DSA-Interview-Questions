'''
There are N Mice and N holes that are placed in a straight line. Each hole can
accommodate only 1 mouse. The positions of Mice are denoted by array A 
and the position of holes are denoted by array B.
A mouse can stay at his position, move one step right from x tox + 1, or
move one step left from x to x — 1. Any of these moves consumes 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole
is minimized.

Return an integer denoting the minimum time when the last nouse gets inside the holes.

Example Input:
M=[-10, -79, -79, 67, 93, -85, -28, -94]
H=[-2, 9, 69, 25, -31, 23, 50, 78 ]

Example Output:
102

'''
class Solution:
    def merge(self,arr,low,mid,high):
        arr1,arr2=arr[low:mid+1],arr[mid+1:high+1]
        k=low
        i=j=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr[k]=arr1[i]
                i+=1
            else:
                arr[k]=arr2[j]
                j+=1
            k+=1
        while i<len(arr1):
            arr[k]=arr1[i]
            k+=1
            i+=1
        while j<len(arr2):
            arr[k]=arr2[j]
            k+=1
            j+=1
    def mergesort(self,arr,low,high):
        if low<high:
            mid=(low+high)//2
            self.mergesort(arr,low,mid)
            self.mergesort(arr,mid+1,high)
            self.merge(arr,low,mid,high)
    def mice(self, M, H):
        N=len(M)
        if N!=len(H): #if number of mice not equal to number of holes
            return -1 
        self.mergesort(M,0,N) #sort the mice array
        self.mergesort(H,0,N) #sort the holes array
        max_time=0 
        for i in range(N):
            max_time=max(max_time,abs(M[i]-H[i])) #stores the max time required by a mouse to get into a hole
        return max_time 
s=Solution()
M=[-10, -79, -79, 67, 93, -85, -28, -94]
H=[-2, 9, 69, 25, -31, 23, 50, 78 ]
print(s.mice(M,H))