class Solution:
    def isValid(self, s: str) -> bool:
        # keep track of opening brackets
        stack = []
        
        # to map closing brackets to their opening brackets
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            # If the character is a closing bracket
            if c in closeToOpen:
                # Check if the stack is not empty and the top of the stack matches the value for close bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  
                else:
                    return False  # Invalid pair, return False immediately
            else:
                # If its an opening bracket, push it onto the stack
                stack.append(c)
        
        # If the stack is empty, all brackets were matched; otherwise, return False
        return True if not stack else False