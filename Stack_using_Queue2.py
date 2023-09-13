'''
Implement Stack using 2 Queues:

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all 
the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.

Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or 
deque (double-ended queue) as long as you use only a queue's standard operations.

'''
from queue import Queue

class MyStack:

    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1,self.q2=self.q2,self.q1

    def pop(self) -> int:
        return self.q1.get()
        

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.qsize()==0