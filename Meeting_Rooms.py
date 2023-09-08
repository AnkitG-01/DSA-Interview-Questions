'''
Meeting Rooms 2

Given an 2D integer array A of size N x 2 denoting time intervals of different
meetings where:
+ A[i][0] = start time of the ith meeting.
+ A[i][1] = end time of the ith meeting.
Find the minimum number of conference rooms required so that all 
meetings
can be done.
Note: If a meeting ends at time t, another meeting starting at time t can use
the same conference room

'''
def solve(meetings):
        start=sorted([i[0] for i in meetings]) #array of meeting start times
        end=sorted([i[1] for i in meetings]) #array of meeting end times
        res,count=0,0
        s=e=0
        while s<len(meetings):
            if start[s]<end[e]: # type: ignore
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res=max(res,count)
        return res
A = [[0, 30],[5, 10],[15, 20]]
print(solve(A))