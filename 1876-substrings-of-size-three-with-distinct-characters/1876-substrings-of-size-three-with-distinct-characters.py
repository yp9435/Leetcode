class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Base case: if the string has less than 3 characters, no valid substrings
        if len(s) < 3:
            return 0

        # Initialize the count of good substrings
        count = 0

        # Use a sliding window of size 3
        L = 0
        R = 2

        while R < len(s):
            # Extract the substring of size 3
            window = s[L:R+1]

            # Check if all characters in the substring are distinct
            if len(set(window)) == 3:  # Using a set to ensure uniqueness
                count += 1

            # Move the window
            L += 1
            R += 1

        return count

        