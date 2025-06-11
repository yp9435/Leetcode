class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        output = []

        for i in nums:
            output.append(prefix)
            prefix *= i
        for i in range(len(nums) -1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output