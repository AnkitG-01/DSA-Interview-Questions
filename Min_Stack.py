'''
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

'''
class MinStack:

    def __init__(self):
        self.st=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.min)==0 or val<=self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.st:
            if self.st[-1]==self.min[-1]:
                self.min.pop()
            self.st.pop()

    def top(self):
        if self.st:
            return self.st[-1]

    def getMin(self):
        if self.min:
            return self.min[-1]
