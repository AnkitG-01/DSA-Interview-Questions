'''
Implementing Stack in python 

'''
class Stack:
    
    #constructor
    def __init__(self, n: int):
        
        # Declare array.
        self.myStack = [0 for _ in range(n)]
        
        # Stack size.
        self.top = -1
        
        # Maximum size.
        self.n = n

    # Push function.
    def push(self, num: int) -> None:
        
        # Check if stack is not full.
        if self.top != self.n - 1:
            
            # Increment stack size and update array.
            self.top += 1
            self.myStack[self.top] = num

    # Pop function.
    def pop(self) -> int:
        
        # Check if stack is not empty.
        if self.top != -1:
            
            # Decrease size and return element.
            self.top -= 1
            return self.myStack[self.top + 1]
        else:
            return -1

    # Top function.
    def Top(self) -> int:
        
        # Check if stack is not empty.
        if self.top != -1:
            
            # Return element.
            return self.myStack[self.top]
        else:
            return -1

    # To check whether stack is empty or not.
    def isEmpty(self) -> int:
        
        # Check if stack is not empty.
        if self.top != -1:
            
            # Return element.
            return 0
        else:
            return 1
        
    # To check whether stack is full or not.
    def isFull(self) -> int:
        
        # Check if stack is not empty.
        if self.top != self.n - 1:
            
            # Return element.
            return 0
        else:
            return 1
St=Stack(5)
St.push(2)
St.push(3)
print(St.pop())
print(St.Top())