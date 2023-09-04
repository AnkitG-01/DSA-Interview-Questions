'''
Binary Search in Bitonic Array:

Given a bitonic sequence A of N distinct elements, write a program to find a 
given element B in the bitonic sequence in O(logN) time.
NOTE A Bitonic Sequence is a sequence of numbers which is first strictly 
increasing then after a point strictly decreasing.

Example Input:
arr=[1,3,4,6,7,5,2,1]
key=2

Example Output:
6

'''
def search(arr,key):
    def bin_search(arr,low,high,key): #binary search
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==key: #checks if mid equals key element
                return mid
            elif key<arr[mid]: #checks if mid greater than key
                high=mid-1
            else: #checks if mid less than key element
                low=mid+1
        return -1

    def peak(arr): #finds the peak element of the bitonic array
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if (mid==0 or arr[mid]>arr[mid-1]) and (mid==len(arr)-1 or arr[mid]>arr[mid+1]): #checks if mid element is greater is it's next and previous element 
                return mid
            elif arr[mid-1]>arr[mid]: #checks if mid is less than it's previous element
                high=mid-1
            else: #checks if mid is less than it's next element
                low=mid+1
        return -1
    
    max_idx=peak(arr)
    target_idx=bin_search(arr,0,max_idx,key) #search the ascending part of the array
    if target_idx!=-1: #if target element is found
        return target_idx
    else: #if target element is not found
        target_idx=bin_search(arr,max_idx+1,len(arr)-1,key) #search the descending part of the array
        return target_idx
print("Enter list")
l=list(map(int,input().split()))
key=int(input("Enter key: "))
print("index = ",search(l,key))