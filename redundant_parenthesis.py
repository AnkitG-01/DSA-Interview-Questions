'''
Check Redundant Brackets

Given a string A denoting an expression. It contains the following operators
+, -, *, /.
Check whether A has redundant braces or not.
NOTE: A will be always a valid expression.

Example Input:
(((a+b))+c)

Example Output:
True

'''
def redundancy(s):
    stack=[]
    operators=['+','-','*','/']
    for c in s: 
        if c==')':
            top=stack.pop()
            redundant=True
            while stack and top!='(':
                if top in operators: #If there is an operator between a pair of opening and closing bracket, set redundant to false 
                    redundant=False
                top=stack.pop()
            if redundant:
                return True
        else:
            stack.append(c)
    return False
st="(((a+b))+c)"
print(redundancy(st))