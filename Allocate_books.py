'''
Allocate Books

Given an array of integers A of size N and an integer B. The College library
has N books. The i th book has A[i] number of pages. You have to allocate
books to B number of students so that the maximum number of pages
allocated to a student is minimum.
1. A book will be allocated to exactly one student.
2. Each student has to be allocated at least one book.
3. Allotment should be in contiguous order, for example: A student cannot be 
allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.
NOTE: Return -1 if a valid assignment is not possible.

Example Input:
arr=[25, 46, 28, 49, 24]
n=5
m=4

Example Output:
71

'''
def findPages(arr, n, m):
    if n<m:
        return -1
    if m==1:
        return sum(arr)
    def count_students(arr,pages): #counts the number of students if each student has to carry a minimum number of pages
        st,pg=1,0
        for i in arr:
            pg+=i
            if pg>pages:
                st+=1
                pg=i
        return st
    low,high=max(arr),sum(arr)
    while low<=high:
        mid=(low+high)//2

        students=count_students(arr,mid)
        if students>m:
            low=mid+1
        else:
            high=mid-1
    return low
books=[25, 46, 28, 49, 24]
n=5
students=4
print(findPages(books,n,students))