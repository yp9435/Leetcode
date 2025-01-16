class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        max_len = 0
        hashmap = {}  # To count character frequencies

        while R < len(s):
            # Increment the frequency of the character at R
            hashmap[s[R]] = hashmap.get(s[R], 0) + 1

            # Check if the current window is valid
            window_size = R - L + 1
            max_freq = max(hashmap.values())  # Maximum frequency of any character in the window
            if window_size - max_freq <= k:
                max_len = max(max_len, window_size)
            else:
                # Shrink the window from the left
                hashmap[s[L]] -= 1
                if hashmap[s[L]] == 0:
                    del hashmap[s[L]]
                L += 1

            # Expand the window
            R += 1

        return max_len