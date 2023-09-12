'''
Reverse a linked list

'''
class Solution:
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node
        return prev