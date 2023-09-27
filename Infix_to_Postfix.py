class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        op_stack=[]
        postfix=""
        priority={'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
        
        for ch in exp:
            
            if ch=='(':
                op_stack.append(ch)
            
            elif ch==')':
                while op_stack[-1]!='(':
                    postfix+=op_stack.pop()
                op_stack.pop()
            
            elif ch=='+' or ch=='-' or ch=='*' or ch=='/' or ch=='^':
                while op_stack and priority[op_stack[-1]]>=priority[ch]:
                    postfix+=op_stack.pop()
                op_stack.append(ch)
            
            else:
                postfix+=ch
        
        while op_stack:
            postfix+=op_stack.pop()
        
        return postfix