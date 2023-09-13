'''
Union of Two Sorted Arrays:

Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.
NOTE: Elements in the union should be in ascending order.

Example 1:

Input:
n = 5,m = 5.
arr1[] = {1,2,3,4,5}  
arr2[] = {2,3,4,4,5}
Output:
 {1,2,3,4,5}

Explanation: 
Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5} 

Example 2:

Input:
n = 10,m = 7.
arr1[] = {1,2,3,4,5,6,7,8,9,10}
arr2[] = {2,3,4,4,5,11,12}

Output: {1,2,3,4,5,6,7,8,9,10,11,12}

Explanation: 
Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1,6,7,8,9,10
Distnict Elemennts in arr2 are : 11,12
Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}
'''
def merge(a,b):
        temp=[]
        n,m=len(a),len(b)
        left,right=0,0
        while left<n and right<m:
            if a[left]<=b[right]:
                if len(temp)==0 or temp[-1]!=a[left]:
                    temp.append(a[left])
                left+=1
            else:
                if len(temp)==0 or temp[-1]!=b[right]:
                    temp.append(b[right])
                right+=1
        while left<n:
            if temp[-1]!=a[left]:
                temp.append(a[left])
            left+=1
        while right<m:
            if temp[-1]!=b[right]:
                temp.append(b[right])
            right+=1
        return temp


print(merge([1,3,5],[0,1,2,4]))