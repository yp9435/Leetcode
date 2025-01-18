class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)  # Use a set for quick lookups
        longest = 0  
        
        for i in numset:  # Iterate directly over the set to avoid duplicates
            if (i - 1) not in numset:  # Start of a new sequence
                length = 1  
                while (i + length) in numset:  # Check the next numbers in the sequence
                    length += 1
                longest = max(longest, length)
        
        return longest