class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def isPalindrome(self, head):
        
        #if the list is empty or it has only one element, it's a palindrome
        if not head or not head.next:
            return True
        
        #find the middle of linked list
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #split and reverse the linked list from the middle 
        prev=None
        curr=slow
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        #if the two linked lists don't match, the list is not palindrome
        p1=head
        p2=prev
        while p2:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True         