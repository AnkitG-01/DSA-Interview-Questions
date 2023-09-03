'''
4 SUM:

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

'''
def fourSum(nums, target):
    n=len(nums)
    nums.sort() #Sort the list first
    res=set()
    
    for i in range(n-3): #1st loop to choose 1st number

        if i>0 and nums[i]==nums[i-1]:
            continue #After sorting, all the duplicate elements will be together so we use this condition to skip the duplicates

        for j in range(i+1,n-2): #2nd loop to choose 2nd number
            if j>i+1 and nums[j]==nums[j-1]:
                continue #After sorting, all the duplicate elements will be together so we use this condition to skip the duplicates

            left=j+1 #left pointer to choose the 3rd number
            right=n-1 #right pointer to choose the 4th number

            #the next part is similar to 2Sum II where the given list is sorted
            while left<right: #base case

                diff=target-(nums[i]+nums[j]+nums[left]) #calculate the diff between the target and the first 3 numbers

                if diff>nums[right]:
                    left+=1 #if the diff is greater than the number pointed by right pointer then increment the left pointer

                elif diff<nums[right]:
                    right-=1 #if the diff is less than the number pointed by right pointer then decrement the right pointer

                else:
                    res.add(tuple(sorted([nums[i],nums[j],nums[left],diff]))) #if the diff is equal to the number pointed by the right pointer then return all 4 numbers
                    #We add the numbers as a sorted tuple so that we can get rid of duplicates
                   
                    while left<right and nums[left]==nums[left+1]:
                        left+=1 #we use this condition to skip the duplicates
                    
                    while left<right and nums[right]==nums[right-1]:
                        right-=1 #We use this condition to skip the duplicates
                    
                    left+=1
                    right-=1
                    #increment left and right pointers to find the rest of the numbers 
    return res
print(fourSum([15,2,5,3,18,11,1,8],14))