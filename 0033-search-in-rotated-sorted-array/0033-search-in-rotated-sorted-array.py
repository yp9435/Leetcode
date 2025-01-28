class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid 

            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # If target is outside the sorted left range, search the right half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:  # Target is within the sorted left range
                    r = mid - 1

            # Otherwise, the right half is sorted
            else:
                # If target is outside the sorted right range, search the left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:  # Target is within the sorted right range
                    l = mid + 1

        # If the target is not found, return -1
        return -1
