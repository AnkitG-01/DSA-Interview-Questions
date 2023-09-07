'''
Intersection of two Arrays:

Find the intersection of two sorted arrays OR in other words, given 2 sorted 
arrays, find all the elements which occur in both arrays.
NOTE For the purpose of this problem (as also conveyed by the sample case),
assume that elements that appear more than once in both arrays should be 
included multiple times in the final output.

Example Input:
arr1=[1,2,3,3,4,5]
arr2=[3,3,5]

Example Output:
[3,3,5]

'''
def intersection(arr1,arr2):
    l1=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            l1.append(arr1[i])
            i+=1
            j+=1
    return l1
arr1=[1,2,3,3,4,5]
arr2=[3,3,4,5]
print(intersection(arr1,arr2))