'''
Swap Adjacent Nodes:

Given a linked list A, swap every two adjacent nodes and return its head. 
NOTE: Your algorithm should use only constant space. You may not modify 
the values in the list; only nodes themselves can be changed.

Example Input:
1->2->3->4
Example Output:
2->1->4->3

'''
class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode=Node(data)
        currNode=self.head
        if currNode:
            while currNode.next:
                currNode=currNode.next
            currNode.next=newNode # type: ignore
        else:
            self.head=newNode

    def swap(self,head):
        temp = Node()
        temp.next = head
        start = head.next
        while temp.next  and temp.next.next:
            ptr1 = temp.next
            ptr2 = temp.next.next
            temp.next = ptr2
            ptr1.next = ptr2.next
            ptr2.next = ptr1
            temp = ptr1
        return start
    
    def print(self,currNode):
        while currNode:
            print(currNode.val)
            currNode=currNode.next

    def main(self):
        arr=[1,2,3,4,5,6,7,8,9]
        for i in arr:
            self.append(i)
        ptr=self.swap(self.head)
        self.print(ptr)

ll=LinkedList()
ll.main()
