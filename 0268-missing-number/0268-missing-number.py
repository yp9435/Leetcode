class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        
        for i in range(n):
            xor ^= i  # XOR with index
            xor ^= nums[i]  # XOR with element in nums

        # XOR with the last number (n) to include it
        xor ^= n
        
        return xor