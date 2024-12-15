class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        pos, neg = 0, 1  # Two pointers: `pos` for positive, `neg` for negative.

        for num in nums:
            if num > 0:
                result[pos] = num
                pos += 2  # Move `pos` pointer to the next positive index.
            else:
                result[neg] = num
                neg += 2  # Move `neg` pointer to the next negative index.
        
        return result