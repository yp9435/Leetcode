class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1 = 0
        xor2 = 0
        n = len(nums)
        for i in range(n-1):
            xor1 = xor1 ^ nums[i]
            xor2 = xor2 ^ (i+1)
        
        xor2 = xor2 ^ n

        return (xor1 ^ xor2) - 1 #idk why -1 but it wont work otherwise