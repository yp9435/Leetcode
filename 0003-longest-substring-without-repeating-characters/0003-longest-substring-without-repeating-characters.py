class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0  # Left pointer of the window
        R = 0  # Right pointer of the window
        max_len = 0  # To store the maximum length
        char_set = set()  # To track characters in the current window

        while R < len(s):  # Iterate until the right pointer reaches the end
            if s[R] not in char_set:
                char_set.add(s[R])  # Add the character to the set
                max_len = max(max_len, R - L + 1)  # Update maximum length
                R += 1  # Move the right pointer
            else:
                char_set.remove(s[L])  # Remove the leftmost character
                L += 1  # Move the left pointer

        return max_len
                