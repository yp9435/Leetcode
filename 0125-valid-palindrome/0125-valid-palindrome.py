class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: left (L) and right (R)
        L = 0
        R = len(s) - 1

        # Loop until the pointers meet in the middle
        while L < R:
            # Skip non-alphanumeric characters on the left
            if not s[L].isalnum():
                L += 1
            # Skip non-alphanumeric characters on the right
            elif not s[R].isalnum():
                R -= 1
            # Check if the characters at L and R (ignoring case) are not equal
            elif s[L].lower() != s[R].lower():
                return False  # Not a palindrome
            else:
                # Move both pointers closer to the center
                L += 1
                R -= 1

        # If we complete the loop without finding mismatches, it's a palindrome
        return True