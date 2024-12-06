class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore's Voting Algorithm
        candidate, count = 0, 0

        # Phase 1
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        
        # Phase 2
        count = 0
        for i in nums:
            if i == candidate:
                count += 1
        
        if count > (len(nums)//2):
            return candidate
        return -1
        