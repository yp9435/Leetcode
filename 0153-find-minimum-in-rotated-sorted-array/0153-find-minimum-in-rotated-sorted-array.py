class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1  
        res = nums[L]  

        while L <= R:
            # If the subarray is already sorted, take the smallest element
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            M = L + ((R - L) // 2)  
            res = min(res, nums[M])  # Update the minimum value

            # Decide which side to search next
            if nums[M] >= nums[L]:  # Left side is sorted
                L = M + 1  # Search in the right half
            else:  
                R = M - 1  # Search in the left half

        return res  
