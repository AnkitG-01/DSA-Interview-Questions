'''
Minimum number of platforms required for a railway:
We are given two arrays that represent the arrival and departure times of trains that stop at the platform. 
We need to find the minimum number of platforms needed at the railway station so that no train has to wait.

Examples 1:

Input: 
N=6
arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00} 
dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}

Output:
3

Explanation: 
There are at-most three trains at a time. The train at 11:00 arrived but the trains which had arrived at 9:45 and 9:55 have 
still not departed. So, we need at least three platforms here.



'''
def calculateMinPatforms(at, dt, n):
    count=1
    at.sort()
    dt.sort()
    count=1
    ans=1
    i=1
    j=0
    while i<len(at) and j<len(dt):
        if at[i]<=dt[j]:
            count+=1
            i+=1
        else:
            count-=1
            j+=1
        ans=max(ans,count)
    return ans