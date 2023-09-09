'''
Merge two sorted linked lists

Use the merge function of merge sort
 
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def mergeTwoLists(self, list1, list2):
        #if both lists empty, return any of the lists
        if not list1 and not list2:
            return list2
        
        #if any of the lists is empty, return the non-empty list
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        #create a linked list to store the merged list 
        head=merged_list=ListNode()

        #similar to the merge function of merge sort
        while list1 and list2:
            if list1.val<list2.val:
                merged_list.next=list1
                merged_list=merged_list.next
                list1=list1.next
            else:
                merged_list.next=list2
                merged_list=merged_list.next
                list2=list2.next
        
        #if list1 hasn't reached the end, copy the rest of the elements       
        if list1:
            merged_list.next=list1
        
        #if list2 hasn't reached the end, copy the rest of the elements
        if list2:
            merged_list.next=list2

        #return the head node of merged list
        return head.next