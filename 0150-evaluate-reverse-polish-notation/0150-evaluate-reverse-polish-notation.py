class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # PUSH A NUMBER AND whne u come across a +-/* pop 2 elements from the stack and do the operation put the answer back in stack
        for token in tokens:
            if token in '+-/*':
                n1, n2 = stack.pop(), stack.pop()
                if token == "+":
                    new = n2 + n1
                elif token == "-":
                    new = n2 - n1
                elif token == "/":
                    new = int(n2 / n1)
                elif token == "*":
                    new = n2 * n1
                stack.append(new)
            else:
                stack.append(int(token))
        return stack[-1]
    
        
        '''stack = [] 
        for c in tokens:
            if c == "+":  
                stack.append(stack.pop() + stack.pop())
            elif c == "-":  
                a, b = stack.pop(), stack.pop()  # order matters for subtraction
                stack.append(b - a) 
            elif c == "*":  
                stack.append(stack.pop() * stack.pop())
            elif c == "/":  
                a, b = stack.pop(), stack.pop()  # order matters for division
                stack.append(int(float(b) / a))  # Perform division and truncate towards zero
            else:
                stack.append(int(c))  # If the token is a number, convert to int and push onto the stack
        return stack[0]'''