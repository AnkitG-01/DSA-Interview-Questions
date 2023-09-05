'''
Count inversions in an array:

Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).

What is an inversion of an array? 
Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

Examples
Example 1:
Input Format: N = 5, array[] = [1,2,3,4,5]
Result: 0
Explanation: we have a sorted array and the sorted array has 0 inversions as for i < j you will never find a pair such that A[j] < A[i]. 
More clear example: 2 has index 1 and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an inversion.

Example 2:
Input Format: N = 5, array[] = [5,4,3,2,1]
Result: 10
Explanation: we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. 
Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions 
and for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.For above given array there is 4 + 3 + 2 + 1 = 10 inversions.

Example 3:
Input Format: N = 5, array[] = [5,3,2,1,4]
Result: 7
Explanation: There are 7 pairs (5,1), (5,3), (5,2), (5,4),(3,2), (3,1), (2,1) and we have left 2 pairs (2,4) and (1,4) as both are not satisfy our condition.

'''
def merge(arr,low,mid,high):
    count=0 #count the pairs
    left=low #pointer of left half of array
    right=mid+1 #pointer of right half of array
    temp=[] #temporary array to store the sorted array
    while left<=mid and right<=high: #storing the elements in a sorted order in temp
        
        if arr[left]>arr[right]:
            count+=((mid+1)-left) #if an element of left array is greater than an element of right array then 
            #increment count by the number of elements in left array after that element including that element 
            # (mid+1) length of left array i is index of current element of left array
            temp.append(arr[right])
            right+=1
        
        else:
            temp.append(arr[left])
            left+=1

    # if elements on the left half are still left
    while left<=mid:
        temp.append(arr[left])
        left+=1

    # if elements on the right half are still left
    while right<=high:
        temp.append(arr[right])
        right+=1

    #transfer all elements from temp to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return count #return value of count

def merge_sort(arr,low,high):
    count=0
    if low>=high: #base case
        return count
    mid=(low+high)//2
    count+=merge_sort(arr,low,mid) #adding value of count from left half
    count+=merge_sort(arr,mid+1,high) #adding value of count from right half
    count+=merge(arr,low,mid,high) #adding value of count from merged array
    return count

def getInversions(arr, n) :
    
    return merge_sort(arr,0,n-1)

print(getInversions([5,3,2,1,4],5))