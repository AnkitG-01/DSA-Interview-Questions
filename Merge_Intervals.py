'''
Merge Overlapping Intervals:

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''
class Solution(object):
    def merge(self, intervals):
        
        intervals.sort() #first we need to sort the intervals
        
        ans=[intervals[0]] #the list with all the merged intervals 

        for start,end in intervals[1:]:
            
            lastend=ans[-1][1] #we are taking the last element of the last interval in the ans array
            
            if lastend>=start:
                ans[-1][1]=max(lastend,end) #if the last element of the last interval of ans is greater than the starting element of the next interval
                #we change the last element of the last interval of ans to max of lastend or last of next interval to merge the two intervals
            
            else:
                ans.append([start,end]) #if the intervals are not overlapping, just add interval to ans 

        return ans
s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))