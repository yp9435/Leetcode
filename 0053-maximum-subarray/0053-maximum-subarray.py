class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # intialise with negative infinity
        max_sum = float('-inf')
        curr_sum = 0

        # Bottom Up Dynamic Programming that looks like greedy approach
        # kadane's algorithm.
        # Big O(n) - Time Complexity

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum