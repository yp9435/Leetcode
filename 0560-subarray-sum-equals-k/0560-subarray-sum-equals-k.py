class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        HashMap = {}
        count = 1
        for i in range(len(nums)):
            HashMap[nums[i]] = k-nums[i] #difference
        
        for i in HashMap:
            if HashMap[i] in HashMap:
                count += 1
                break
        return count