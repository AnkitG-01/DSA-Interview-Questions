'''
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        l=0
        ptr=head

        #calculate the length of linked list
        while ptr:
            ptr=ptr.next
            l+=1
        
        #if linked list is empty return None
        if not l:
            return None
        
        #if length equals n then we have to remove the head node, so return list from next of head
        if l==n:
            return head.next
        
        ptr=head
        for i in range(l-n-1):
            ptr=ptr.next
        ptr.next=ptr.next.next #remove the nth node from last
        return head