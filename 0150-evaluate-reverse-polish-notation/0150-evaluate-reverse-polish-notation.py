class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
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
        return stack[0] 