class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Lengths of s1 and s2
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        # If s1 is longer than s2, no permutation is possible
        if len_s1 > len_s2:
            return False
        
        # Create frequency dictionaries for s1 and the first window of s2
        patternCount = {}
        windowCount = {}
        
        for char in s1:
            patternCount[char] = patternCount.get(char, 0) + 1
        
        for char in s2[:len_s1]:
            windowCount[char] = windowCount.get(char, 0) + 1
        
        # Sliding window across s2
        for i in range(len_s2 - len_s1):
            # Check if current window matches the pattern
            if windowCount == patternCount:
                return True
            
            # Slide the window: remove the leftmost character
            left_char = s2[i]
            windowCount[left_char] -= 1
            if windowCount[left_char] == 0:
                del windowCount[left_char]
            
            # Add the next character in the window
            right_char = s2[i + len_s1]
            windowCount[right_char] = windowCount.get(right_char, 0) + 1
        
        # Check the last window
        return windowCount == patternCount
