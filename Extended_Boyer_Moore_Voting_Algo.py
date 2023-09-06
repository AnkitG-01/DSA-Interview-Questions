'''
Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]

'''
class Solution(object):
    def majorityElement(self, nums):

        count1=count2=0
        candidate1,candidate2=0,-1

        for i in nums:

            if count1==0 and i!=candidate2:
                count1=1 #set count1 as 1 if current element is not candidate2
                candidate1=i #also set candidate1 as current element

            elif count2==0 and i!=candidate1:
                count2=1 #set count2 as 1 if current element is not candidate1
                candidate2=i #also set candidate2 as current element

            elif candidate1==i:
                count1+=1 #if current element is candidate1, increment count1 by 1

            elif candidate2==i:
                count2+=1 #if current element is candidate2, increment count2 by 1

            else:
                #if current element is neither candidate1 nor candidate2, decrement both counts by 1
                count1-=1
                count2-=1

        count1,count2=0,0 #again set counts to zero to calculate the frequencies of both candidates

        for i in nums:

            if i==candidate1:
                count1+=1

            if i==candidate2:
                count2+=1

        ans=[]
        n=len(nums)//3

        if count1>n:
            ans.append(candidate1)

        if count2>n:
            ans.append(candidate2)
            
        return ans