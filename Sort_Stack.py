'''
Sort a stack using recursion

'''
def insert(stack,x):
    if len(stack)==0 or stack[-1]<x: #base case
        stack.append(x) #if stack is empty or top of stack is less than the inserting element, then return
        return
    #if top of stack is greater than the inserting element
    p=stack.pop() #pop from stack
    insert(stack,x) #recursive call
    stack.append(p) #insert the popped element back
def sortStack(stack):
    if len(stack)==0: #base case
        return #if stack is empty return
    p=stack.pop() #pop and empty the stack first 
    sortStack(stack) #recursive call
    insert(stack,p) #insert the popped element back in order