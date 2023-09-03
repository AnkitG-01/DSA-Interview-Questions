'''
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        ptr1,ptr2=l1,l2
        num1=num2=0
        i=j=0
        while ptr1:
            num1=num1+(10**i)*ptr1.val
            i+=1
            ptr1=ptr1.next
        while ptr2:
            num2=num2+(10**j)*ptr2.val
            j+=1
            ptr2=ptr2.next
        
        num=num1+num2
        head=temp=ListNode()

        if not num:
            return temp
        
        while num>0:
            d=num%10
            num=num//10
            head.next=ListNode(d)
            head=head.next
        return temp.next