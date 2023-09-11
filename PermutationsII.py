'''
Permutations II:

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''
class Solution:
    def permuteUnique(self, nums):
        res=[]
        perm=[]
        hmap={}

        for num in nums:
            hmap[num]=1+hmap.get(num,0) #add the elements and their occurences to the hashmap

        def dfs(): #depth first search helper function to find th permutations

            if len(perm)==len(nums): #base case
                res.append(perm[:]) #if length of perm and input lists are same, add a copy of perm to res and return
                return
            
            for n in hmap: #iterating through all the distinct elements in the hashmap
                
                if hmap[n]>0: #if frequency of element is more than zero
                    perm.append(n) #add that element to perm
                    hmap[n]-=1 #decrement that element's frequency by 1

                    dfs() #recursive function call

                    hmap[n]+=1 #add the element's frequency back to the hashmap 
                    perm.pop() #pop back the elements added to the perm

        dfs() #call the depth first search function
        return res
s=Solution()
print(s.permuteUnique([1,1,4,5]))