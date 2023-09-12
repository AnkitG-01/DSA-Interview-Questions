'''
Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

'''
class Solution:
    def rotateRight(self, head, k):
        if head==None or head.next==None or k==0:
            return head
    
        last=head
        l=1
        while last.next:
            last=last.next
            l+=1
        k=k%l
        last.next=head #convert the singly linked list to circular linked list
        temp=head
        for i in range(l-k-1):
            temp=temp.next
        ans=temp.next
        temp.next=None
        return ans