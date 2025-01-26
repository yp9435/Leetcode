class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize L & R
        L = 0
        R = len(nums) - 1

        while L <= R:
            # avoiding integer overflow
            M = L + ((R - L) // 2)
            
            # Check if the target is at the middle
            if nums[M] == target:
                return M 
            elif target < nums[M]:
                R = M - 1             # search in the left half
            else:
                L = M + 1             # search in the right half
                
        return -1
